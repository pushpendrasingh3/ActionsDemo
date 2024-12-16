import os

filepath = "argocd-cicd-setup/"
path = os.listdir(filepath)
for content in path:
    print(content)

current = "2.0.3"
new     = "2.0.4"
total =  0
for content in path:
    counter = 0
    
    try :
        with open(filepath + content, "r", encoding="utf-8") as file:
            result = file.read()
            counter = result.count(current)
    except:
        #print(content, " I cannot read the content")
        newPath = os.listdir(filepath+content)
        for newContent in newPath:
            print("filename: "+ newContent)
            try:
                with open(filepath + content +"/"+ newContent, "r", encoding="utf-8") as newInFile:
                  newResult = newInFile.read()
                  counter = newResult.count(current)
            except:
                print(newContent, "I cannot read the content")
                pass
            else:
                newResult = newResult.replace(current, new)
                with open(filepath + content +"/"+ newContent, "w", encoding="utf-8") as newInFile:
                  newInFile.write(newResult)
                if counter:
                    print(newContent, ":", counter, "changes")
                    total +=1 
        pass
    else:
        result = result.replace(current, new)
        with open(filepath + content, "w", encoding="utf-8") as newFile:
          newFile.write(result)
        if counter:
            print(content, ":", counter, "changes")
            total +=1
print("Totally", total, "files changed.")
     
    
