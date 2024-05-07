const { ApolloServer } = require('apollo-server')
const { allCourses, genres} = require('./database')
const { typeDefs } = require('./schema');
const { Query } = require("./resolvers/query")
const { Course } = require("./resolvers/course")
const { Genre } = require("./resolvers/genre")

const server = new ApolloServer({ typeDefs, 
    resolvers: {Query, Course, Genre}, context: {allCourses, genres}});

server.listen().then(({url}) => console.log(`Server is running at ${url}`));