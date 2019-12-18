langDict = {
    "C++" : "C++ was the main language I used for computer games development. This was because speed, optimisation and memory management were important factors into making a 3D graphical game run smoothly at 30-60 FPS. I like the freedom C++ allows.",

    "Python" : "I am a big fan of Python after using C# and C++ for so long as it makes little work of scripting, automating, web-scraping and string manipulation. What takes tens of lines of boilerplate in a C-based language, can take one line in Python.",

    "C#" : "C# was the first programming language I used. With automatic memory management and the protections offered by the compilar, it was a great language to learn object oriented programming in. I dabbled with .NET technologies such as XNA in a college project before it's disconinuation that made development for Windows and Xbox 360 easier.",

    "Java" : "During my education I have used Java for Android application development, as well as during a module on Object Oriented Software Development in the higher diploma course. With automatic memory management and it's portability it makes for a great general-purpose language.",

    "JavaScript" : "I have used JavaScript for web development, alongside HTML5 and CSS, and the superset TypeScript using Angular7 for creating my website.",

    "TypeScript" : "I have used TypeScript with Angular 7 to create my website. Being a superset of JavaScript, it's also valid JavaScript code."
}

position = "Software Developer"
website = "Indeed.com.au"
jobListing = "C++ C# Python"

def getList(dictionary): 
    return dictionary.keys() 

def getLangString(dic, jListing):
    langString = ""

    langList = getList(dic)

    for lang in langList:
        if lang in jobListing:
            langString = langString+" "+dic[lang]

    return langString



cover = """Dear hiring manager, 

I would like to express my interest in the position of {job} listed on {site}. With a Graduate Diploma in Science in Computing (Systems and Information Technology Services), and a Bachelor’s (Honours) degree in Computer Games Development, I believe that I could be an asset to your company, and a good fit for the position.
 
I enjoy challenging work along with engaging in projects that expand my knowledge-set and skills. Learning new languages and development practices are important to me. I am a quick learner, and adapt well to any environment.

I have used C#, C++, Python, Java and JavaScript mainly. {langStrings}

I received the State Street International (Ireland) Student of the Year Award at Level 8 for academic excellence when graduating with First-Class Honours from the Institute of Technology Carlow (Ireland) in November 2019 with a Graduate Diploma in Science in Computing (Systems and Information Technology Services). 

My previous work experience includes retail management. This has greatly helped me develop the ability to solve problems while under pressure, communicate effectively and manage challenging customers through de-escalation. I am very patient and can remain calm in stressful situations, and think outside of the box where necessary. 
 
I’ve attached a copy of my resume, and can be reached on my mobile at 0458894863, or via email at emailforjmorris@gmail.com. 
 
Thank you for your time and consideration. I look forward to speaking with you about this opportunity. 
 
Yours sincerely, 
Jonathan Morris """

if __name__ == "__main__":
    print(cover.format(job=position,site=website, langStrings=getLangString(langDict, jobListing)))
