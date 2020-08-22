# Masonite + Inertia.js with Vue.js

This is a demo (which is going to be improved to show different use cases !) of a Masonite app
with Inertia.js. The Inertia.js adapter has been developed by @josephmancuso (https://gist.github.com/josephmancuso/6528fe8ef9cb2f6cf25ccd19852ee7f1).

This can be cloned now to play with the demo =) !

<p align="center">
<img src="https://i.imgur.com/rEXcoMn.png" width="160px"> 
</p>

<p align="center">

<img src="https://travis-ci.org/MasoniteFramework/masonite.svg?branch=master">
<img src="https://img.shields.io/badge/python-3.4+-blue.svg" alt="Python Version"> <img src="http://pepy.tech/badge/masonite?1" alt="License">  <img src="https://img.shields.io/github/license/MasoniteFramework/masonite.svg" alt="License"> 
<img src="https://coveralls.io/repos/github/MasoniteFramework/core/badge.svg?branch=master#" alt="License">

</p>

## About Masonite

The modern and developer centric Python web framework that strives for an actual batteries included developer tool with a lot of out of the box functionality with an extremely extendable architecture. Masonite is perfect for beginner developers getting into their first web applications as well as experienced devs that need to utilize the full potential of Masonite to get their applications done.

Masonite works hard to be fast and easy from install to deployment so developers can go from concept to creation in as quick and efficiently as possible. Use it for your next SaaS! Try it once and you’ll fall in love.

- Having a simple and expressive routing engine
- Extremely powerful command line helpers called `craft` commands
- A simple migration system, removing the "magic" and finger crossing of migrations
- A great Active Record style ORM called Orator
- A great filesystem architecture for navigating and expanding your project
- An extremely powerful Service Container (IOC Container)
- Service Providers which makes Masonite extremely extendable

## Learning Masonite

Masonite strives to have extremely comprehensive documentation. All documentation can be [Found Here](https://docs.masoniteproject.com/v/v2.1/) and would be wise to go through the tutorials there. If you find any discrepencies or anything that doesn't make sense, be sure to comment directly on the documentation to start a discussion!

If you are a visual learner you can find tutorials here: [MasoniteCasts](https://casts.masonite.dev)

Also be sure to join the [Slack channel](http://slack.masoniteproject.com/)!

## How to install this demo

```
$ pip install -r requirements
```

And for Vue.js apps with Inertia client

```
$ npm install
```

## How to run this demo

```
$ npm run dev
```

Now we can run the server like we normally do:

```
$ craft serve
```

When we go to our homepage we will see we see:

```
Home Page
```

Congratulations! We have now setup Inertia in our project! Refer to the [InertiaJS Documentation](https://inertiajs.com/routing)
