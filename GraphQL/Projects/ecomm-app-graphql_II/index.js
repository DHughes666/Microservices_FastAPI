const { ApolloServer } = require('apollo-server')
const { allCourses, genres, reviews} = require('./database')
const { typeDefs } = require('./schema');
const { Mutation } = require('./resolvers/mutation')
const { Query } = require("./resolvers/query")
const { Course } = require("./resolvers/course")
const { Genre } = require("./resolvers/genre")

const server = new ApolloServer({ typeDefs, 
    resolvers: {Query, Mutation, Course, Genre}, 
    context: {allCourses, genres, reviews}});

server.listen().then(({url}) => console.log(`Server is running at ${url}`));