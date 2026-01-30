---
title: Data Programming
subtitle: University of Washington, Spring 2026
---

+++ { "part": "abstract" }

The world has become data-driven. Domain scientists and industry increasingly rely on data analysis to drive innovation and discovery; this reliance on data is not only restricted to science or business, but also is crucial to those in government, public policy, and those wanting to be informed citizens. As the size of data continues to grow, everyone will need to use powerful tools to work with that data. In this course, students will learn to:

1. **Design and build programs** to handle data analysis tasks small and large.
1. **Process and structure data** to organize complex data using data structures.
1. **Analyze and visualize data** to find patterns, make plots, and share results.
1. **Apply professional practices** to effectively write, test, and maintain software.

+++

:::{schedule}
:::

This course is designed to support students who have **no prior programming experience**. If you have programming experience, take Intermediate Data Programming (CSE 163) instead!

## Why should we learn?

The education you receive in this course can help prepare you for programming jobs, but [this isn't the only purpose for computing education](https://computinged.wordpress.com/2021/11/26/computer-science-was-always-supposed-to-be-taught-to-everyone-but-not-about-getting-a-job-a-historical-perspective/). Education is not only about yourself and your personal gain, but also about all of us and our capacity to live together as a community.

The University of Washington acknowledges the Coast Salish peoples of this land, the land which touches the shared waters of all tribes and bands within the Duwamish, Puyallup, Suquamish, Tulalip and Muckleshoot nations. Among the traditions of the Coast Salish peoples is a value for the connectedness between all living things and a recognition of the [unique ways that each of us comes to know things](https://youtu.be/O6sS1ZI8dDk).

> Modern education has the idea that we all need to know the same thing. At the end of the lesson, everyone will know the same thing. That's why we have tests, that's why we have quizzes, that's why we have homework: to ensure we all know the same thing. And that's powerful—that's important—within a certain context.
>
> But for native culture, the idea that each listener divines or finds their own answer, their own meaning, their own teaching from the story is equally powerful—that each person needs to be able to look at the world and define it for themselves within their culture and then also find a way to live in that world according to the teachings of their people in their culture.

We are responsible for each others' success
: Everyone has a right to feel like they belong in this course. We'll need to act with compassion and caring to collaborate with each other. Although we will need more than just unexamined commitments to collaboration, listening, empathy, mindfulness, and caring, the following guidelines offer a starting point for ensuring compassion toward each other [@10.37514/PER-B.2022.1824].

  - Listen with intention to understand first and form an opinion only after you fully understand.
  - Take responsibility for intended and unintended effects of your words and actions on others.
  - Mindfully respond to others' ideas by acknowledging the unique value of each contribution.

: You should expect and demand to be treated by your classmates and teachers with respect. If any incident occurs that challenges this commitment to a supportive, diverse, inclusive, and equitable environment, please let the instructor know so the issue can be addressed. Should you feel uncomfortable bringing up an issue with the instructor directly, meet our advisors during [quick questions](https://www.cs.washington.edu/academics/ugrad/advising#qqs) or contact the [College of Engineering](https://www.engr.washington.edu/bias).

We recognize everyone has unique circumstances
: Do not hesitate to contact the instructor by private post or [appointment](https://kevinl.info/meet/). The sooner we are made aware of your circumstances, the more we can help. Extenuating circumstances include work-school balance, familial responsibilities, religious observations, military duties, unexpected travel, or anything else beyond your control that may negatively impact your performance in the class.
: It is the policy and practice of the University of Washington to create inclusive and accessible learning environments consistent with federal and state law. If you have already established accommodations with [Disability Resources for Students](https://depts.washington.edu/uwdrs/) (DRS), activate your accommodations via myDRS so we can discuss how they will be implemented in this course. If you have a temporary health condition or permanent disability that requires accommodations, contact DRS directly to set up an Access Plan.
: Washington state law requires that UW develop a policy for accommodation of student absences or significant hardship due to reasons of faith or conscience, or for organized religious activities. The UW's policy, including more information about how to request an accommodation, is available at [Religious Accommodations Policy](https://registrar.washington.edu/staffandfaculty/religious-accommodations-policy/). Accommodations must be requested within the first two weeks of this course using the [Religious Accommodations Request form](https://registrar.washington.edu/students/religious-accommodations-request/).

We believe everyone wants to learn
: Education is about shaping your identity as much as it is about learning things. In school, the consequences of making mistakes are relatively small. But the habits you form now—repeated over days, weeks, months, or years—determine who you will be in the future. Now is the best time to practice honest habits.
: We ask that you do not claim to be responsible for work that is not yours. When you receive substantial help from someone else, include a citation. Don't post your solutions publicly. Most importantly, don't deprive yourself or others of the learning opportunities that we've created in this course. Allegations of misconduct by students may be referred to the appropriate campus office for investigation and resolution.
: Academic honesty reflects the trust (or the lack thereof) between students and teachers. We do our best to design the course in ways that ensure trust, but we know our systems are not perfect. If you submit work in violation of these policies but bring it to the attention of the instructor within 72 hours, you may resubmit your own work without further consequence. Rather than blame students, we want to fix or replace broken systems that compel students to lose trust.

## How does learning occur?

In a traditional classroom, you attend class while a teacher lectures until time is up. Then, you go home and do the important work of applying concepts toward practice problems or assignments on your own. Finally, you take an exam to show what you know.

Today, we know that there are more effective ways to learn science, engineering, and mathematics [@10.1073/pnas.1319030111]. Learning skills like software engineering and algorithm analysis requires **deliberate practice**: a learning cycle that starts with sustained motivation, then presents tasks that build on prior knowledge, and concludes with immediate, personalized feedback. Each module in the course will involve several different activities that are designed so that we can make the most of our class time together.

In groups during class and quiz section, collaborate on the in-class guided practice.
: In PollEverywhere during lecture, **correctly answer all questions**.
: In Gradescope during section, **correctly answer all questions**.

On your own after class, apply what you learned in the homework and project.
: Practice applying your learning by completing **Exercises** (not submitted for credit).
: In Gradescope, submit your completed **Homework** assignment for the week.

During certain class meetings, complete the quest (quick test) to show what you've learned.
: On paper, complete a 30-minute quest individually before reworking it with a group.
: At the end of the quarter, complete the paper final exam, which reassesses course concepts.

All homework is designed to be completed with what has been taught in class. Keep your homework within the scope of what has been taught. Work that is found to be out-of-scope will receive deductions. Repeated use of out-of-scope content is considered academic misconduct. Help from sources outside the course may be used only for clarifying concepts, supporting debugging, or explaining problems at a high level. Writeups should all be your own words and ideas; you will not be penalized for grammar or mechanics as long as we understand what you are saying and your arguments are reasonable.

Encouraged
: Discussing examples shown in class. These examples are learning materials.
: Working with a TA to work on a task and resolve a particular problem.
: Talking with other students without sharing code or details to reproduce code.

Permitted with caution
: Working alongside one or more other people on a homework or project.
: Sharing or generating small snippets of code not specific to any assignment part.

Prohibited
: Obtaining solutions to any assignment part in any form for any reason.
: Giving, receiving, obtaining, or generating a walkthrough to an assignment.
: Posting solutions to an assignment in a public place even after the course is over.

Expect to spend 4 hours in class and 8 hours outside of class working on this course. Some weeks may require more or less time than other weeks. If you find the workload is significantly exceeding this expectation, talk to your TA.

## How is this course graded?

Final grades are determined through a three-step process designed to measure your core knowledge, reward your hard work, and encourage consistent participation.

Quests and Final Exam
: This is the most significant part of your grade. Each of the 3 graded quests contribute 15% toward your final grade. The final exam is worth the remaining 55% of your grade and contains 4 parts. The first 3 parts of the final exam correspond to the 3 graded quests. If your score on a part of the final is higher than your score on the matching quest, the better final part will replace your quest grade.

Homework
: Homework scales the score you earned from your quests and final exam. If you complete all your homework perfectly, you keep 100% of your score from the first step. However, if you don't do any of the homework at all, your score from the first step will be cut in half. Performance between 0 and 100 will scale this effect accordingly.
: Homework scores will be rounded up. Each score will be rounded up to the next 10% interval. For example, any score greater than 90% on will be rounded up to 100%. Note that a score of exactly 90% remains 90%.

Lightweight Activities
: Lightweight activities and participation determine how your final grade is rounded. By default, your grade on the 4.0 scale is rounded down to the nearest decimal point (for example, a 3.89 becomes a 3.8). If you complete at least 90% of the lightweight activities, your grade will be rounded normally instead (a 3.85 becomes a 3.9).

All coursework except for the final exam have mechanisms for demonstrating improvement. Learning in this course involves feedback loops where you try something, get feedback, and then try again. Grades are based on what you eventually learn through this process. Each homework assignment has a single resubmission period for students to improve their work.
