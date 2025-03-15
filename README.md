# Paycheck to Paycheck
### _An app for those to make each paycheck a little less stressful._
#### By Oliver Lear Sigwarth

[![Paycheck to Paycheck Logo](./angular/assets/images/logo/logo_cropped_small.png)]()

---

Paycheck to Paycheck is a budgeting app to help you with your finances in a
window most people are familiar with: the time between paychecks. Knowing how
much you can spend, and when, is crutial to many people with tight budgets. At
Paycheck to Paycheck, we hope to automate this process for you so you never
have to stand in a the grocery store wondering if your card will be declined.
Our simple-to-use app will help you track your spending, when your are 
spending it, and when you are getting paid next. We hope to make your life a
little less stressful by helping you keep track of your finances.

---

## Features
- 💵 **Budgeting**: See what your income allows you to spend.
- ⌛️ **Timing**: Know when you are getting paid next, and when you can spend the
              money you have.
- 🏦 **Understand Your Holdings**: See how you can save, or pay off debt, with
                                the money you have.
- 📱 **Simple Interface**: Easy to use, easy to understand, and easy to navigate.

## Get Started

1. 🌐 Head over to the [Paycheck to Paycheck]() website. (Not yet launched)
2. 🤝 Create an account.
3. 💵 Start tracking your finances!

#### It's as easy as that!

---

## Progress

### Milestone 1 - 2/14/25

For the first milestone, I have created the structure for the project. The
stack for the project includes:

- **Frontend**: Angular
- **Backend**: Django
- **Database**: PostgreSQL with Django ORM

The project will employ an Agile methodology. Implementing this methodology 
took much of the first milestone's efforts. Below you will see how the 
Software Development Life Cycle (SDLC) will be implemented in the project.

![Paycheck to Paycheck Roadmap](./assets/p2p_roadmap.png)

This roadmap will be continuously updated and you can go to the projects tab
to see the latests developments.

The major developments in software can be broken down between the front-end 
and the back-end.

#### Front-end

The modular structure of Angular has been put in place. There are the 
dependencies required to make a fully-fledged web app. The beginning
components are starting to be developed. The most important components like 
the nav bar and footer have taken precedence.

The personality of website must be shown in the front-end. Knowing this, there
have been various design choices made about the look and feel of the website.
The website should have:

- Credibility
- Consistency
- Clarity

I am implementing this personality by have a soft color scheme. I am using a
color palette of soft greens and white to convey a pure and clean intention.
You can see the personality of the site with the beginnings of the web 
interface shown below.

![Milestone One Homepage](./assets/p2p_milestone_one_home_page.png)

#### Back-end

A whole lot of work is needed for the back-end. The beginning of making models
has been paramount in the first milestone. They are the backbone of our data.
Given the program is using ORM, the models are especially important in serving
a dual purpose of a back-end object and a database object. The major models 
have been started. These would include:

- User
  - Holding foreign keys and basic data
- Dates
  - Due dates
  - Recurring dates
- Income
  - One-time income
  - Recurring income
- Bills
  - One-time bills
  - Recurring bills
- Holdings
  - Debts
  - Savings
- Paychecks
  - Incorporating all the above

Given the tightly interconnected nature of the models, none can be said to be
fully complete at this time. The models are going to be continuously developed
in the beginning stages of the project.

#### Watch the Progress

Below is a video about the progress made in the first milestone.

[![Milestone One Progress](./assets/youtube_video_icon.png)](https://youtu.be/vJyiV0lwHPQ)

_Or go to this [this link](https://youtu.be/vJyiV0lwHPQ) (https://youtu.be/vJyiV0lwHPQ)_

---

### Milestone 2 - 3/14/25

The second milestone was a big step forward. Between that time, about 600 
commits were added. The progress was made in both the front-end and back-end.
Look below to see the progress made in each area.

#### Both Front-end and Back-end

A massive boilerplate issue was encountered with pure HTTP requests. The 
ceasing of listening and then immediately calling for an update made it clear
that WebSockets were needed. For both the front-end and back-end, models and 
controllers were made to handle the WebSocket connections. The front-end
using Angular services and the back-end using **Django Channels**. This type 
of communication was seamlessly integrated into the app.

#### Front-end

There has been major strides in multiple components in the front-end. The 
first is the input for income and bills. Using Reactive Programming, the tree
of components takes input from the lowest level component and passes and 
refines it to the top level component. The top level component validates the
inputs and then passes them to the back-end.

Authentication, a beating heart feature for the app, was added this milestone.
Though not fully implemented, this functionality, in conjunction with session
data binding, will allow inputs like bills and income to be saved to a given 
user. As a core feature, this completion sets us up for a strong next 
milestone.

Features added:
- **Input for Income**: The user can input their income.
  - One-time income
  - Recurring income
  - Wage income
- **Input for Bills**: The user can input their bills.
  - One-time bills
  - Recurring bills
- **Authorization**: Getting user credentials and validating them.
  - Input validation
    - Filled fields
    - Valid emails
    - Matching passwords
    - Terms of service agreement
  - Signing up
    - Signup console
    - Signup WebSockets connection
  - Logging in
    - Login console
    - Login WebSockets connection
  - Authentication response
    - WebSockets return user's authentication status

##### New Components

Below you can see the UI for the newly integrated components.

##### Bill and Income Inputs

![Milestone Two Bill and Income Inputs](./assets/p2p_milestone_two_inputs.png)

##### Authentication Consoles

![Milestone Two Authentication Consoles](./assets/p2p_milestone_two_auth_page.png)

#### Back-end

The back-end kept pace with the front-end during this sprint. The models for
the back-end grew more complex with new refined models. The relationships 
between users and their bills and income are now held in a single object each.

- **Bill history**: The history of bills is now held in a single object.
  - One-time bills
  - Recurring bills
- **Income history**: The history of income is now held in a single object.
  - One-time income
  - Recurring income
  - Wage income

Using Django Channels, the back-end was able to seamlessly implement two-way
communication. Controllers, or views in Django, are replaced with consumers in
Django Channels. Each entity is associated with its own consumer.

##### New Consumers

- Generic WebSocket consumer
- Auth consumers
  - Login consumer
  - Signup consumer
- Bill consumers
  - One-time bill consumer
- Income consumers
  - One-time income consumer
  - Recurring income consumer

##### Dictionary Parsing

Sending payloads from the front-end may include fields that are not 
applicable to the back-end models. To handle this, specialized dictionary
parsers were created. These parsers take the attributes of a normalize 
front-end JSON payloads, finds appropriate class fields, and creates an object
using the dictionary data.

#### Watch the Progress

Below is a video about the progress made in the second milestone.

[![Milestone Two Progress](./assets/youtube_video_icon.png)](https://youtu.be/n5RN0N9qiiM)

_Or go to this [this link](https://youtu.be/n5RN0N9qiiM) (https://youtu.be/n5RN0N9qiiM)_

---
