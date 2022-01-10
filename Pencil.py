class Pencil:
    def __init__(self, pointDurability, lengthValue, eraserDurability):
        self.pointDurability = pointDurability
        self.lengthValue = lengthValue
        self.eraserDurability = eraserDurability 
        self.default_durability = pointDurability

    def set_pointDurability(self, pointDurability):
        self.pointDurability = pointDurability

    def get_pointDurability(self):
        return self.pointDurability

    def set_lengthValue(self, lengthValue):
        self.lengthValue = lengthValue

    def get_lengthValue(self):
        return self.lengthValue

    def set_eraserDurability(self, eraserDurability):
        self.eraserDurability = eraserDurability

    def get_eraserDurability(self):
        return self.eraserDurability

    def write(self, userText):
        textAbleToBeWritten = ''
        for letter in userText:
            if self.pointDurability < 0:
                self.pointDurability = 0
            if self.pointDurability == 0:
                if self.lengthValue != 0:
                    self.sharpen()
                if self.pointDurability == 0:
                    #letter = " "  
                    return textAbleToBeWritten          
            if letter.isupper():            # if upper case letter, pencil point degrades by 2
                self.pointDurability -= 2
            if letter.islower():
                self.pointDurability -= 1        # if lower case letter, pencil point degrades by 1
            textAbleToBeWritten += letter
        return textAbleToBeWritten

    def sharpen(self):
        self.lengthValue = self.lengthValue - 1
        self.pointDurability = self.default_durability
    
    def erase(self, userText, wordToErase):
        
        if self.eraserDurability == 0:      # if eraser is dull
            print("Eraser is dull!")
            return userText
        newWord = ""
        userText = newWord.join(userText.rsplit(wordToErase, 1))        # splitting string into separate words 

        self.eraserDurability -= 1      # eraser durability decreases by one
        return userText
        
    
        
    
            

if __name__ == "__main__":


    ################################## Manual insertion by user ##################################

    # pointDurability = input("Point Durability: ")
    # pointDurability = int(pointDurability)
    # lengthPencil = input("Length of Pencil: ")
    # lengthPencil = int(lengthPencil)
    # eraserDurability = input("Eraser Durability: ")
    # eraserDurability = int(eraserDurability)

    # pencil1 = Pencil(pointDurability, lengthPencil, eraserDurability)

    # print("Insert word(s): ")
    # userText = input()
    # pencil1.write(userText)
    # print("-----------------------------")
    # print("Pencil Statistics")
    # print("Updated Point Durability: ", pencil1.get_pointDurability())
    # print("Updated Length of Pencil: ", pencil1.get_lengthValue())
    # print("Updated Eraser Durability: ", pencil1.get_eraserDurability())
    # print(userText)

    # print("Word to Erase: ")
    # wordToErase = input()
    # userText = pencil1.erase(userText, wordToErase)
    # print("Input with word erased: ", userText)
    # print("Eraser Durability: ", pencil1.get_eraserDurability())

    # print("Do you want to erase a word? (y/n)")
    # continueErasing = input()
    # while (continueErasing == "y"):
    #     print("Word to Erase: ")
    #     wordToErase = input()
    #     userText = pencil1.erase(userText, wordToErase)
    #     print("Input with word erased: ", userText)
    #     print("Eraser Durability: ", pencil1.get_eraserDurability())
    #     print("Do you want to continue erasing? (y/n)")
    #     continueErasing = input()

    ################################################################################################

    ################################## Automated Test Case ##################################
    pointDurability = 10
    lengthPencil = 1
    eraserDurability = 1
    pencilTest1 = Pencil(pointDurability, lengthPencil, eraserDurability)
    print("-----------------------------")
    print("Initial Pencil Statistics")
    print("Point Durability: ", pencilTest1.get_pointDurability())
    print("Length of Pencil: ", pencilTest1.get_lengthValue())
    print("Eraser Durability: ", pencilTest1.get_eraserDurability())
    print("-----------------------------")

    userText = "I love Comcast"
    print("Test #1: ", userText)
    userText = pencilTest1.write(userText)
    print("-----------------------------")
    print("Pencil Statistics")
    print("Updated Point Durability: ", pencilTest1.get_pointDurability())
    print("Updated Length of Pencil: ", pencilTest1.get_lengthValue())
    print("Updated Eraser Durability: ", pencilTest1.get_eraserDurability())
    print("Input saved: ", userText)
    print("-----------------------------")

    
    print("Word to Erase: ")
    wordToErase = input()
    userText = pencilTest1.erase(userText, wordToErase)
    print("Input with word erased: ", userText)
    print("Eraser Durability: ", pencilTest1.get_eraserDurability())

    print("Do you want to erase a word? (y/n)")
    continueErasing = input()
    while (continueErasing == "y"):
        print("Word to Erase: ")
        wordToErase = input()
        userText = pencilTest1.erase(userText, wordToErase)
        print("Input with word erased: ", userText)
        print("Eraser Durability: ", pencilTest1.get_eraserDurability())
        print("Do you want to continue erasing? (y/n)")
        continueErasing = input()
    





