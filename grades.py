def gradingSystem():
    name= input("Enter Student's Name: ")
    Mat, Phy, Geo, Chem = map(int, input("Enter the marks for maths, physics, geo ,Chem in that order: ").split())

    if Mat < 0 or Phy < 0 or Geo < 0 or Chem < 0 or Mat > 100 or Phy > 100 or Geo > 100 or Chem > 100:
        print("Invalid Marks, please check and try again ")
        return

    avg = (Mat + Phy + Geo + Chem) / 4

    if 0 <= avg <= 30:
        grade = 'D'
    elif 31 <= avg <= 50:
        grade = 'C'
    elif 51 <= avg <= 70:
        grade = 'B'
    elif 71 <= avg <= 100:
        grade = 'A'
    else:
        print("Invalid average")
        return

    print("maths: ", Mat)
    print("Physics: ", Phy)
    print("geo: ", Geo)
    print("Chem: ", Chem)
    print("Average: ", avg)
    print("Grade: ", grade)
    print(f"{name} has an everage marks of {avg} which is a grade of {grade}")


gradingSystem()
