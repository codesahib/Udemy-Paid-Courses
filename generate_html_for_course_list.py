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
    body{
        background-color: #FAF9F6;
    }

    #intro{
        background-color: #E8F5FA;
        display: flex;
        flex-direction: column;
        width: 70%;
        border-radius: .625rem;
        font-size: 1.25rem;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
        padding: .625rem
    }

    .courseContainer {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .course{
        display: flex;
        width: 70%;
        margin:  .625rem .625rem;
        box-shadow: 0 0 .3125rem .125rem gray;
        background-color: #f8f5ea;
        justify-content: center;
    }

    .courseButton {
        width: fit-content;
        align-self: center;
        background-color: #344765;
        color: white;
        border-radius: .625rem;
        min-height: 1.875rem;
        min-width: 6.25rem;
        animation: glowing 1300ms infinite;
    }

    .courseButton:hover{
        cursor: pointer;
    }

    .courseHeading {
        color: #333333;
        font-family: &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;
        font-size: 1.125rem;
        font-weight: bold;
        text-align: center;
    }

    .courseAbout {
        justify-content: center;
    }

    .imageContainer, .detailContainer{
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: .625rem 1.25rem;
    }

    .imageContainer {
        border-right:  .0625rem solid gray;
    }

    h3 {
        text-align: center;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    }

    h1 {
        margin: 1.875rem
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
    <center>
        <div id="intro">
            <p>Welcome to <a href="https://udemyfreecoursehere.blogspot.com/">udemyfreecoursehere.blogspot.com</a></p>
            <p>Here you'll find premium certifaction courses for free. The courses come with a certification which can be added to resume/LinkedIn to get a boost in career.</p>
            <h3>You'll always find updated Udemy course list here. So bookmark <a href="https://udemyfreecoursehere.blogspot.com/">this</a> page to get latest updates daily</h3>
        </div>
        <h1>Free course list for 
     """
    
html += date_today

html += """</h1>
    </center>
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
</body>
</html>
"""


# print(html)

f = open('output.html','w',encoding='utf-8')
f.write(html)
f.close()