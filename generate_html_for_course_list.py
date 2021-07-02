from datetime import date

today = date.today()
date_today = today.strftime("%d/%m/%Y")

course_list=[\
"Complete JAVASCRIPT with HTML5,CSS3 from zero to Expert-2021||https://www.udemy.com/course/build-responsive-website-using-html5-css3-js-and-bootstrap-p/?ranMID=39197&ranEAID=nN98ER4vNAU&ranSiteID=nN98ER4vNAU-aqxgqDV6CwjDraFr1LBDBw&utm_source=aff-campaign&LSNPUBID=nN98ER4vNAU&utm_medium=udemyads&couponCode=4D07D2277F23DC426AC0",\
"Becoming A Recruitment And Selection Specialist||https://www.udemy.com/course/first-steps-into-recruitment-and-selection/?ranMID=39197&ranEAID=nN98ER4vNAU&ranSiteID=nN98ER4vNAU-XJrnTq21VYUHEHv1kj9ZOw&LSNPUBID=nN98ER4vNAU&utm_source=aff-campaign&utm_medium=udemyads&couponCode=JUNE.2021"]


space_4="    "
space_8 = space_4+space_4
space_12 = space_8+space_4
space_16 = space_8+space_8

html = """
<html>
<head>
<meta content="width=device-width, initial-scale=1" name="viewport"></meta>
<style>
    .courseContainer {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .course{
        display: flex;
        width: 70%;
        margin:  10px 10px;
        box-shadow: 0px 0px 5px 2px gray;
        background-color: #FAF9F6;
        justify-content: center;
    }

    .imageContainer, .detailContainer{
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 10px 20px;
    }

    .imageContainer {
        border-right:  1px solid gray;
    }

    .courseButton {
        width: fit-content;
        align-self: center;
        background-color: #344765;
        color: white;
        border-radius: 10px;
        min-height: 30px;
        min-width: 100px;
        animation: glowing 1300ms infinite;
    }

    .courseButton:hover{
        cursor: pointer;
    }

    .courseHeading {
        color: #333333;
        font-family: &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
    }

    .courseAbout {
        justify-content: center;
    }

    h3 {
        margin-top: 100px;
        text-align: center;
    }

    @keyframes glowing {
        0% {
          background-color: #344765 ;
          box-shadow: 0 0 5px #ADD8E6;
        }
        100% {
          background-color: #4ea7c2;
          box-shadow: 0 0 5px #ADD8E6;
        }
    }
</style>
</head>
<body>
    <h1> Udemy free course list for """
    
html += date_today

html += """</h1>
    <p>Presenting Udemy free courses. The courses come with a certification which can be added to resume/LinkedIn to get a boost in career.</p>
    <div class="courseContainer">
"""

course_list_html = []
html_template_for_course = "\n"+space_8+"<div class='course'>\n"+space_12+"<div class='detailContainer'>\n"+space_16+"<span class='courseHeading'>__heading__</span><br /><button class='courseButton' onclick='window.open(\"__url__\")'>Get Course</a></button>\n"+space_12+"</div>\n"+space_8+"</div>"

for course in course_list:
    c = course.split('||')
    heading = c[0]
    url = c[1]

    html_template_for_course = html_template_for_course.replace("__heading__",heading)
    html_template_for_course = html_template_for_course.replace("__url__",url)

    course_list_html.append(html_template_for_course)
    
    html_template_for_course = html_template_for_course.replace(heading,'__heading__')
    html_template_for_course = html_template_for_course.replace(url,'__url__')

html += '\n'.join(course_list_html)

html += """
    </div>
    
    <h3>Bookmark this page to get latest updates daily</h3>
</body>
</html>
"""


# print(html)

f = open('output.html','w',encoding='utf-8')
f.write(html)
f.close()