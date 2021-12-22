print(" \n Hello, Welcome to Brainy Trivia!!!")
print("\n____________________________________\n")
ans = input(" \n Are you ready for some interesting quiz (yes /no):")
print("\n____________________________________\n")
score = 0
total_q = 10
if ans.lower() == "yes":

    ans = input("\n1. Who is the founder of Microsoft? ")
    if ans.lower() == "bill gates":
        score += 1
        print("Correct")
        print("=================================")
    else:
        print("Incorrect")
        print("=================================")

    ans = input("\n2. Which team in IPL 2018 won the championship title? ")
    if ans.lower() == "csk" or ans.lower() == "chennai super kings":
        score += 1
        print("Correct")
        print("=================================")
    else:
        print("Incorrect")
        print("=================================")

    ans = input("\n3. Which is the world's tallest statue? ")
    if ans.lower() == "unity" or ans.lower() == "statue of unity":
        score += 1
        print("Correct")
        print("=================================")
    else:
        print("Incorrect")
        print("=================================")

    ans = input("\n4. Which youtube channel has the most subscibers? ")
    if ans.lower() == "t-series" or ans.lower() == "tseries" or ans.lower() == "t series":
        score += 1
        print("Correct")
        print("=================================")
    else:
        print("Incorrect")
        print("=================================")

    ans = input("\n5. Which is the longest river in the world? ")
    if ans.lower() == "nile river" or ans.lower() == "river nile":
        score += 1
        print("Correct")
        print("=================================")
    else:
        print("Incorrect")
        print("=================================")

    ans = input("\n6. Which is the Garden City of India? ")
    if ans.lower() == "bangalore" or ans.lower() == "bengaluru":
        score += 1
        print("Correct")
        print("=================================")
    else:
        print("Incorrect")
        print("=================================")

    ans = input("\n7. Which is the Tallest building in the world? ")
    if ans.lower() == "burj khalifa":
        score += 1
        print("Correct")
        print("=================================")
    else:
        print("Incorrect")
        print("=================================")

    ans = input("\n8. Who is the author of HARRY POTTER? ")
    if ans.lower() == "j.k.rowling" or ans.lower() == "j.k rowling" or ans.lower() == "jk rowling":
        score += 1
        print("Correct")
        print("=================================")
    else:
        print("Incorrect")
        print("=================================")

    ans = input("\n9.Who is known as \"MISSILE MAN OF INDIA\"? ")
    if ans.lower() == "dr.a.p.j.abdul kalam" or ans.lower() == "apj abdul kalam" or ans.lower() == "abdul kalam" or ans.lower() == "dr apj abdul kalam" or ans.lower() == "dr abdul kalam" or ans.lower() == "a.p.j. abdul kalam":
        score += 1
        print("Correct")
        print("=================================")
    else:
        print("Incorrect")
        print("=================================")

    ans = input("\n10. Name of the actor who acted in \"Mr.Bean\"? ")
    if ans.lower() == "rowan atkinson" or ans.lower() == "rowan":
        score += 1
        print("Correct")
        print("\n=================================\n")
    else:
        print("Incorrect")
        print("\n=================================\n")

print("\nThank you for playing!!, you got ", score, " question correct!!! ")
mark = (score/total_q) * 100
print("\nMark:", str(mark) + "%")
print("\n____________________________________\n")
print("\nThank you for playing the brainy quiz!!! \n"
      "Hope, see you soon  with many more quiz..!!! ")
print("\n====================================\n")