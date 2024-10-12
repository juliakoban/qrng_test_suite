import os

ASCII_TYPE  = "ascii"
BINARY_TYPE = "binary"

def file_type( path ):
    try:
        with open( path, "r" ) as f:
            content = f.read( )
        return ASCII_TYPE
    except UnicodeDecodeError:
        return BINARY_TYPE

def load_binary_file( path ):
    with open( path, "rb" ) as f:
        content = f.read( 20000 // 8  )
    sequence = ''.join(f'{byte:08b}' for byte in content)
    # print( len( sequence ) )
    return sequence

def load_ascii_file( path ):
    with open( path, "r" ) as f:
        content = f.read( )
    sequence = ''.join(f'{ord(char):08b}' for char in content)
    # print( sequence )
    return sequence

def load_file( path ):
    if not os.path.exists( path ):
        raise FileNotFoundError( f"File { path } does not exist." )
    type = file_type( path )
    if type == ASCII_TYPE:
        return load_ascii_file( path )
    return load_binary_file( path )
 
