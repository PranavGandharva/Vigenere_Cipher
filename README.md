# Vigenere_Cipher
# Encryption and Decryption with Vigenere Cipher:
The Vigenere cipher is frequently referred to as a substitution cipher. It is the most straightforward of its sort. It is also referred to as a polyalphabetic cipher. There are letters in English that have possible shifts ranging from 0 to 26. Every ciphertext stands in for a letter in the plaintext. Via plain text communication, the Vigenere cipher employed various monoalphabetic substitutions. 

The plaintext is encrypted starting with the first letter using mod 26, followed by the second letter, and so on. This procedure is repeated until the whole text has been encrypted. A key is required to encrypt the communication. Typically, a recurring keyword serves as the key.
The Vigenere cipher can be broken primarily using the Kasiski, Friedman, and Kerckhoff methods. 

We employ Kerckhoff's technique to decipher the cipher text. To decrypt the cipher, the first step is to determine the key length. The cipher text is first written, and write the copy of the entire cipher text below is offset by a specific number.

Therefore, we can find the total number of coincidences. The keyword length calculated by the number of places that get displaced results in the most occurrence. Also, by calculating the greatest common divisor of displaced places to get the most occurrences.
# Program Output:
# Step 1:
Ciphertext:
NMZFVNEQYINMZJIRJCRWYIQZXURVEXUEAFXNIEJOKICZRMXUVVKARIIGJRNMTGVUITXFKLGXFKVKRTKLKRRUXNICFWYMOZPOXLFJZLRCEZXRIXNIBICGJGVVZLRKSXTRUSYXELGQXUVWNMCZRZLRWICQBDITXFUYXMAXXNIYRYTGUZRMSSKLKFBRXYHNEZKVFNEYWRVRYTRROORTKSGCBLRMEZVVOGNEKOVYESURRRGZYNCPEWNNLOQCRWYEAPXNMAXXULRIFAXUVQOKUKLGZRUSTIFFMZWRVQYXBDIWYVKIRMXVPEXURXNIREXXYFKIJXUVTGTRIWZSGYMYKVIPHIYZIBMAXXNEGJLKEFRAUQNELGHNXVKEGVVILNEGKSSSVORTZRMXUVQYESVPEXBJLUVRSYZMSJSCLRIICEFKLKKVIPGRQNLGXURHYLRUSTIJZXNXUVTGTRIWHCYRXKVNUZOGRWVUQNDIXMPRMZWRVQKHYZOKPLKLGXQRRBIEJLGHOVITGYFWKPLJLGHBNIJSAKLKANPSBIENEYXUZWMMECMTPRRKAIJZXNLVJITIZZIYSEYEJWUVMTLRIXAVASIKRFYEJSJVHGRQVMZLRIXXMPBIJSEWSXGRUMTXBYETHVEKUZRIXNICIIIMBLWVEPBIZARJIZXBNSXOGFXXEPVLKVBLXOXCISBIQLRKBCVGZIQCCJMSWMIYYKLKVARQKANJNGRRWMTRNEHOXQLPEECGIGVRUESSAXXNIYZWZSSKLKWHIZOZBIWHYGKLKKVIPNIEJIRJFVISIQKSNEIVZGRVJLKHPFQVPRKIRCVEUAMEZIYMAKSNIERRZIPVHKRGJHOHYZXZPRKSNIYGYYWUVAGWNESXTURRGRQYEJFRVRCLNKAKWUFYRHPRPRSIVVNIEVEVYCZPZINTLKVVEEYQNCPYGUFSRSHKAKWGYIXTNJWVSEKLGHOVITQNUIUYGWSXTNIMYAUVVKWUVAGWTFMTKGFN
# Step 2:
Number of displacements for most coincidences between the range 2 to 30:
![image](https://github.com/PranavGandharva/Vigenere_Cipher/assets/16937531/c2a1ba95-9a86-4c3c-8a04-448683b2f348)
# Step 3:
The highest number of coincidences:
![image](https://github.com/PranavGandharva/Vigenere_Cipher/assets/16937531/51c2c261-4a7a-4917-bf5f-12fa91b49031)
# Step 4:
The encryption key and final plain text:
![image](https://github.com/PranavGandharva/Vigenere_Cipher/assets/16937531/47b47b95-954b-4b45-b817-0a81ab12b29b)

