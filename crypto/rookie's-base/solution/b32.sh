state="CCSC{Ang3R_Is_A_POt3nt_Sp1C3}"
for i in {1..25}; do
   state=$(echo "$state" | base32)
done
echo "Encoded:"
echo "$state"
echo "$state" >> encoded-message.txt

for i in {1..25}; do
   state=$(echo "$state" | base32 -d)
done

echo "Decoded"
echo "$state"
