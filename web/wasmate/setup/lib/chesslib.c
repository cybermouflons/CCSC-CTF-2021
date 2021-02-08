///////////////////////////////////////////////////////////////////////////////////
//                                                                               //
//                                  Variables                                    //
//                                                                               //
///////////////////////////////////////////////////////////////////////////////////
//                                                                               //
//    S - side                                                                   //
//    E - en passant square                                                      //
//    V - move structure                                                         //
//    L - move list structure                                                    //
//    Q - search info structure                                                  //
//                                                                               //
//    b - board array                                                            //
//                                                                               //
//    d - move direction                                                         //
//  v.f - source square                                                          //
//  v.t - target square                                                          //
//  v.p - piece                                                                  //
//  v.y - piece type                                                             //
//  v.r - step vector ray                                                        //
//  v.x - capture                                                                //
//  v.c - captured square                                                        //
//  v.K - skip square                                                            //
//  v.R - rook square                                                            //
//  v.o - promoted piece                                                         //
//  v.e - evaluation score                                                       //
//  v.s - move score                                                             //
//                                                                               //
//  q.n - nodes                                                                  //
//  q.m - best move                                                              //
//  q.s - best score                                                             //
//                                                                               //
///////////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////////
//                                                                               //
//                                Piece encoding                                 //
//                                                                               //
///////////////////////////////////////////////////////////////////////////////////
//                                                                               //
//  emSq, P+, P-, K, N, B, R, Q                                                  //
//     0,  1,  2, 3, 4, 5, 6, 7                                                  //
//                                                                               //
//  w = 8  b = 16  virgin = 32                                                   //
//                                                                               //
//  wP : P+ | w = 9                                                              //
//  wK :  K | w = 11    wKv : wK | virgin = 43                                   //
//  wN :  N | w = 12                                                             //
//  wB :  B | w = 13                                                             //
//  wR :  R | w = 14    wRv : wR | virgin = 46                                   //
//  wQ :  Q | w = 15                                                             //
//                                                                               //
//  bP : P- | b = 18                                                             //
//  bK :  K | b = 19    bKv : bK | virgin = 51                                   //
//  bN :  N | b = 20                                                             //
//  bB :  B | b = 21                                                             //
//  bR :  R | b = 22    bRv : bR | virgin = 54                                   //
//  bQ :  Q | b = 23                                                             //
//                                                                               //
///////////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////////
//                                                                               //
//                                   Functions                                   //
//                                                                               //
///////////////////////////////////////////////////////////////////////////////////
//                                                                               //
//  M(S, V m)/U(S, V m) - make/unmake move                                       //
//                                                                               //
//        S - side                                                               //
//      V m - move                                                               //
//                                                                               //
//  G(S, E, l, x) - generate moves                                               //
//                                                                               //
//      S - side                                                                 //
//      E - e.p.                                                                 //
//      l - move list                                                            //
//      x - all moves/only captures flag                                         //
//                                                                               //
///////////////////////////////////////////////////////////////////////////////////
//                                                                               //
//  B(S) - evaluate position                                                     //
//                                                                               //                     
//      S - side                                                                 //
//                                                                               //
///////////////////////////////////////////////////////////////////////////////////
//                                                                               //
//  X(S, E, a, k, d, Q *q) - search position                                     //
//                                                                               //
//      S - side                                                                 //
//      E - e.p.                                                                 //
//      a - alpha                                                                //
//      k - beta                                                                 //
//      d - depth                                                                //
//   Q *q - pointer to search info                                               //
//                                                                               //
///////////////////////////////////////////////////////////////////////////////////
//                                                                               //
//  R(S, E, a, k) - quiescence search                                            //
//                                                                               //
//      S - side                                                                 //
//      E - e.p.                                                                 //
//      a - alpha                                                                //
//      k - beta                                                                 //
//                                                                               //
///////////////////////////////////////////////////////////////////////////////////
//                                                                               //
//  Y(S, E, *m) - parse move                                                     //
//                                                                               //
//      S - side                                                                 //
//      E - en passant square                                                    //
//     *m - move string e.g. "e2e4"                                              //
//                                                                               //
///////////////////////////////////////////////////////////////////////////////////
//                                                                               //
//  P() - print board                                                            //
//                                                                               //
///////////////////////////////////////////////////////////////////////////////////

#include <stdio.h>
#include <string.h>
#include <emscripten.h>

#include "chesslib.h"

/*********************************************************************************\
;---------------------------------------------------------------------------------;
;                              BOARD REPRESENTATION                               ;
;---------------------------------------------------------------------------------;
\*********************************************************************************/
 
int b[129] = {  // 0x88 board + centers positional scores

    54, 20, 21, 23, 51, 21, 20, 54,    0,  0,  5,  0, -5,  0,  5,  0, 
    18, 18, 18, 18, 18, 18, 18, 18,    5,  5,  0,  0,  0,  0,  5,  5,
     0,  0,  0,  0,  0,  0,  0,  0,    5, 10, 15, 20, 20, 15, 10,  5,
     0,  0,  0,  0,  0,  0,  0,  0,    5, 10, 20, 30, 30, 20, 10,  5,    
     0,  0,  0,  0,  0,  0,  0,  0,    5, 10, 20, 30, 30, 20, 10,  5,
     0,  0,  0,  0,  0,  0,  0,  0,    5, 10, 15, 20, 20, 15, 10,  5,
     9,  9,  9,  9,  9,  9,  9,  9,    5,  5,  0,  0,  0,  0,  5,  5,
    46, 12, 13, 15, 43, 13, 12, 46,    0,  0,  5,  0, -5,  0,  5,  0
};

// promoted pieces
char c[] = { [0] = ' ', [4] = 'n', [5] = 'b', [6] = 'r', [7] = 'q'};

char u[] = ".-pknbrq-P-KNBRQ";

// move offsets
static const int m[] = {
   15,  16,  17,   0,
  -15, -16, -17,   0,
    1,  16,  -1, -16,   0,
    1,  16,  -1, -16,  15, -15, 17, -17,  0,
   14, -14,  18, -18,  31, -31, 33, -33,  0, 
    3,  -1,  12,  21,  16,   7, 12
},

// piece weights
w[] = { 0, 0, -100, 0, -300, -350, -500, -900, 0, 100, 0, 0, 300, 350, 500, 900 };

/*********************************************************************************\
;---------------------------------------------------------------------------------;
;                                MOVE GENERATION                                  ;
;---------------------------------------------------------------------------------;
\*********************************************************************************/

static inline void M(int S, V m)  // MAKE MOVE
{
    b[m.R] = b[m.c] = b[m.f] = 0; b[m.t] = m.p & 31;

    if(!(m.R & 0x88)) b[m.K] = S + 6;
    
    if(m.y < 3)
    {
        if(m.t + m.r + 1 & 128) b[m.t] = S + m.o;
    }
}


static inline void U(int S, V m)  // TAKE BACK
{
    b[m.R] = S + 38; b[m.K] = b[m.t] = 0; b[m.f] = m.p; b[m.c] = m.x;
}

static inline int B(int S)  // EVALUATE POSITION
{
    int s = 0; int i = 0, p;
    
    do
    {
        if((p = b[i]))
        {
            s += w[p & 15]; // material score
            (p & 8) ? (s += b[i + 8]) : (s -= b[i + 8]); // positional score
        }
    }
    
    while((i = (i + 9) & ~0x88));

    return (S == 8) ? s : -s;
}

static inline int G(int S, int E, L *l, int x)  // GANARATE MOVES
{
    V v; v.o = 0; int d; l->c = 0; v.f = 0;
    
    do  // loop over board pieces
    {
        v.p = b[v.f];
        
        if(v.p & S)
        {
            v.y = v.p & 7; d = m[v.y + 30];
            
            while((v.r = m[++d])) // loop over directions
            {
                v.t = v.f; v.K = v.R = 128;
               
                do  // loop over squares
                {
                    v.t += v.r; v.c = v.t;
                    
                    if(v.t & 0x88) break;
                    if(v.y < 3 && v.t == E) v.c = v.t ^ 16; v.x = b[v.c];
                    if(E - 128 && b[E] && v.t - E < 2 && E - v.t < 2) return 0;
                    if(v.x & S || v.y < 3 && !(v.r & 7) != !v.x) break;
                    if((v.x & 7) == 3) return l->c = 0;
				    
                    M(S, v);  // make move
                    
                    if(v.y < 3)
                    {
                        if(v.t + v.r + 1 & 128)
                        {
                            b[v.t] |= 7; v.o = b[v.t] & 7;
                        };
                    }
                    
                    do
                    {
                        v.s = B(S); // evaluate position for move ordering
                        if(x && v.x) { l->m[l->c] = v; l->c++; }
                        else if(!x) { l->m[l->c] = v; l->c++; }
                        
                        (v.o < 4) ? v.o = 0: v.o--;
                    }
                    
                    while(v.y - b[v.t]-- & 7 && b[v.t] & 4);
                    
                    U(S, v);  // take back
                    
                    v.x += v.y < 5;
                    
                    if(v.y < 3 && 6 * S + (v.t & 112) == 128 ||
                    (((v.p & ~24) == 35) & (d == 13 || d == 15)) && v.R & 0x88 &&
                    b[v.R = (v.f | 7) - (v.r >> 1 & 7)] & 32 &&
                    !(b[v.R ^ 1] | b[v.R ^ 2]))
                    { v.x--; v.K = v.t;}
                }
                
                while(!v.x);
            }
        }
    }
    
    while((v.f = (v.f + 9) & ~0x88)); return 1;
}

/*********************************************************************************\
;---------------------------------------------------------------------------------;
;                                      SEARCH                                     ;
;---------------------------------------------------------------------------------;
\*********************************************************************************/

int R(int S, int E, int a, int k)  // QUIESCENCE SEARCH
{
    int score = B(S);
    
    if(score >= k) return k;
    if(score > a) a = score; 
	
	L l[1];
	
	if(!G(S, E, l, 1)) return 10000;  // checkmate evaluation
	
	for(int i = 0; i < l->c; i++)  // loop over move list
    {   
        for(int n = i + 1; n < l->c; n++)
        {
            // order moves to reduce number of traversed nodes
            if(l->m[i].s < l->m[n].s)
            {
                V v = l->m[i];
                l->m[i] = l->m[n];
                l->m[n] = v;
            }
        }
        
        M(S, l->m[i]);  // make move
        int s = -R(24 - S, l->m[i].K, -k, -a);  // recursive quiescence call
        U(S, l->m[i]);  // take back

        if(s >= k) return k;
        if(s > a) { a = s; }
    }
    
    return a;
}

static int X(int S, int E, int a, int k, int d, Q *q)  // SEARCH POSITION
{
    L l[1];  int x = a; V m;  // x - old alpha
    
    if(!d) return R(S, E, a, k);
    if(!G(S, E, l, 0)) return 10000;  // checkmate evaluation
    
    for(int i = 0; i < l->c; i++)  // loop over move list
    {   
        for(int n = i + 1; n < l->c; n++)
        {
            // order moves to reduce number of traversed nodes
            if(l->m[i].s < l->m[n].s)
            {
                V v = l->m[i];
                l->m[i] = l->m[n];
                l->m[n] = v;
            }
        }
        
        M(S, l->m[i]);  // make move
        int s = -X(24 - S, l->m[i].K, -k, -a, d - 1, q);  // recursive search call
        U(S, l->m[i]);  // take back

        q->m = l->m[i];  // store best move so far

        if(s >= k) return k;
        if(s > a) { a = s; m = l->m[i]; }
    }
    
    if(a != x) q->m = m;  // store best move
    
    return a;
}

int T(char c) // PIECE ID
{
    char* p = &u[0];
    while(*p != c) p++;
    return p - &u[0];
}

void A(int *S, int E, char *p)  // PARSE FEN
{
    for(int i = 0; i < 129; i++) b[i] = 0;

    int f = 0; int r = 7;

    do {
        if(*p >= 'a' && *p <= 'z')  b[(7 - r) * 16 + f++] = T(*p)+16;
        if(*p >= 'A' && *p <= 'Z')  b[(7 - r) * 16 + f++] = T(*p);
        if(*p >= '0' && *p <= '9') f += *p - '0';
        if(*p == '/') { f = 0; r--; }
        p++;
    } while(*p != ' ' && *p != '\0');

    if (*p == '\0') return;    
    (*++p == 'w') ? (*S = 8) : (*S = 16);
    
    while(*p != ' ' && *p != '\0') p++;
    if (*p == '\0') return;
	if(*p != '-') E = (7 - ((p[1] - '0') - 1)) * 16 + (p[0] - 'a');
}

void P()  // PRINT BOARD
{
    for(int i = 0; i < 128; i++)
    {
        if(!(i % 16)) printf(" %d  ", 8 - (i / 16));
        printf(" %c", ((i & 8) && (i += 7)) ? '\n' : u[b[i] & 15]);
    }
    
    printf("\n     a b c d e f g h\n\n");
}

int C(char *fen) // CHECMKMATE CHECK FROM FEN
{
    Q q[1];
    int S = 8, E = 128, d = 2;

    A(&S,E,fen);
    
    int my_score = X(S, E, -10000, 10000, 2, q);


    if(my_score == 10000 || my_score == -10000) return S;
    return 0;
}

int logger(char *input) {
   char buf[strlen(input)+31];
   sprintf(buf, "console.log('[WASMLogger]: %s');", input);
   return emscripten_run_script_int(buf); 
}

extern int check_mate(char* fen) {
    BoardChecker checker;
    checker.is_mate = &C;
    checker.logger = &logger;
   
    strcpy(checker.fen, fen);
    return checker.is_mate(checker.fen);
}
