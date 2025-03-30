# HooHacks2025
REP-Rundown <br>
Too long, didn't read? Get informed. Get the rundown of your representative.

## Inspiration
Many Americans are interested in engaging with politics in the current day and age but lack the time and willingness to express an effort to do relevant research on the topic. As a result, many give up and remain in a perpetual state of apathy, or better yet, proclaim their own political efficacy where there is none. We built Rep-Rundown to tackle this problem at a level often overlooked by citizens: their congressional district. Many people cannot name the house member representing their district or the policies and actions that affect their daily lives. Civic responsibility need not start at the Thanksgiving table or a Twitter post, but instead at the 10 digits and public records made public about all 431 members of Congress' lower chamber. 

## What it does
Given a user-provided zip code, our project returns a "rundown" of the corresponding House of Reps member. This includes the representative's name, political party, congressional district, and a summary about their recent activity.

## How we built it
The backend was built on Python using scraping libraries such as mechanize, beautiful soup, and requests. The front-end work was done with HTML, CSS, and JavaScript. Front and back-end were integrated with Flask.

## Challenges we ran into
Scraping for data from the sites that provided information about representatives from zip code was challenging due to many of the site queries providing non-standardized results. Furthermore, We had to learn front-end development and its connection to a python backend entirely from scratch. Elements of front-end took time to learn, grasp, and apply, which took time. We hoped to source text generation for more detailed information about representatives from Meta's Llama model, but did not have enough time to implement this.

## Accomplishments that we're proud of
This was our first hackathon, and we are proud of not ripping each other's hair out and producing a working project. This was also the first time either of us have done anything with front-end, and we learned a lot about formatting and design.

## What we learned
* Front end :')
* Front to back-end integration between Python and HTML using Flask
* Web scraping

## What's next for REP-Rundown
In order to provide even more useful information in a digestible manner, we would look into providing a list of representatives' keystone policies, stances, and notable actions in an even more user-friendly interface. The goal is to have a resource where  users can get to know the most important information about a representative in a matter of minutes and be able to retain the essential details. Doing this would require better NLP summarization, website hosting, and more infrastructure outside the scope of the project's current time limit but would elevate the use of REP-Rundown to taller heights and even shorter attention-spans.

