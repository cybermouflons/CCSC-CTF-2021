import dis, marshal, sys, types
import codecs
import io

def show_file(f):
    print("""
==========================
Disassembling Code Object:
==========================
    """)
    magic = f.read(4)
    moddate = f.read(4)
    print("magic %s" % (codecs.encode(magic, 'hex')))
    print("moddate %s " % (codecs.encode(moddate, 'hex')))

    try:
        code = marshal.load(f)
        show_code(code)
    except Exception as e:
        print("Error while loading code:")
        print(e)
    
def show_code(code, indent=''):
    indent += '   '
    show_hex("code", code.co_code, indent=indent)
    dis.dis(code.co_code)
    print("%sconsts" % indent)
    print("%sargcount %d" % (indent, code.co_argcount))
    print("%snlocals %d" % (indent, code.co_nlocals))
    print("%sstacksize %d" % (indent, code.co_stacksize))
    print("%sflags %04x" % (indent, code.co_flags))
    print("%snames %r" % (indent, code.co_names))
    print("%svarnames %r" % (indent, code.co_varnames))
    print("%sfreevars %r" % (indent, code.co_freevars))
    print("%scellvars %r" % (indent, code.co_cellvars))
    print("%sfilename %r" % (indent, code.co_filename))
    print("%sname %r" % (indent, code.co_name))
    print("%sfirstlineno %d" % (indent, code.co_firstlineno))
    show_hex("lnotab", code.co_lnotab, indent=indent)
    for const in code.co_consts:
        if type(const) == types.CodeType:
            show_code(const, indent+'   ')
        else:
            print("   %s%r" % (indent, const))

    
def show_hex(label, h, indent):
    h = codecs.encode(h, 'hex')
    if len(h) < 60:
        print("%s%s %s" % (indent, label, h))
    else:
        print("%s%s" % (indent, label))
        for i in range(0, len(h), 60):
            print("%s   %s" % (indent, h[i:i+60]))

with open(sys.argv[1], "rb") as f:
    frames = f.read().split(b"\n==========\n")
    for fr in frames:
        if fr != b"":
            show_file(io.BytesIO(fr))
