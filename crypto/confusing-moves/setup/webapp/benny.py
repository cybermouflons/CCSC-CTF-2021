import subprocess
import importlib
import sys

from webapp.lcg import PRNG

def parse_pgn(pgn_string: str, prng: PRNG, internal_pypi_url: str, public_pypi_url: str):
    
    # Generate "random" package name
    package_name = prng.next_as_hex()

    # Download dependencies...
    logs = ""

    internal_pypi_host = internal_pypi_url.split("//")[1].split("/")[0].split(":")[0]
    public_pypi_host = public_pypi_url.split("//")[1].split("/")[0].split(":")[0]
    command = ['pip', 'install', '--index-url', f'{public_pypi_url}/simple', '--extra-index-url', f'{internal_pypi_url}/simple/', '--trusted-host', f'{internal_pypi_host}', '--trusted-host', f'{public_pypi_host}', package_name]
    
    logs += "=> " + " ".join(command) + "\n"
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    out, err = process.communicate()
    logs += out.decode("utf-8").rstrip()
    logs += err.decode("utf-8").rstrip()

    if err != b"":
        return False, [], logs

    # Parse pgn
    logs += "\n=> Benny is running his python scripts ...."
    thrown_exception = False
    try:
        import pgn
        # importlib.reload(pgn)

        parsed_games = pgn.loads(pgn_string)
        logs += "\n=> Result from parsing: {0}".format(parsed_games)
    except Exception as e:
        logs += "\n[ERROR] Error parsing provided pgn ...."
        logs += "\n{0}: {1}".format(type(e).__name__, e)
        thrown_exception = True

    # Try to delete module
    try:
        del sys.modules["pgn"]
        del pgn
    except Exception:
        pass
    
    if thrown_exception:
        return False, [], logs
    
    logs += "\n[SUCCESS] PGN parsed successfully!" 

    # Uninstall depdencies
    command = ['pip', 'uninstall', '-y', package_name]
    
    logs += "\n=> " + " ".join(command) + "\n"
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    out, err = process.communicate()
    logs += out.decode("utf-8").rstrip()
    logs += err.decode("utf-8").rstrip()

    return True, parsed_games, logs
    
