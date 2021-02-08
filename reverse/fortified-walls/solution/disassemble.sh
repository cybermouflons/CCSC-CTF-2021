docker build . -t fortified-walls-solution
cp ../public/fortified-walls.tar.gz .
tar -xf fortified-walls.tar.gz
echo 'test' | docker run  --rm -v $(pwd):/chall -it fortified-walls-solution:latest
python disass.py bytecode.pyc
