typedef struct { int f, t, p, y, x, c, r, R, K, o, e, s; } V;  // Move variables
typedef struct { V m[256]; int c; } L;  // Move list
typedef struct { int s; V m; } Q;  // Search info
typedef struct BoardChecker {
    char fen[128];
    int (*is_mate)(char *);
    int (*logger)(char *);
} BoardChecker;

static inline void M(int S, V m);
static inline void U(int S, V m);
static inline int G(int S, int E, L *l, int x);
static int X(int S, int E, int a, int k, int d, Q *q);
int R(int S, int E, int a, int k);
int T(char c);
void A(int *S, int E, char *p);
int C(char *fen);
void P();