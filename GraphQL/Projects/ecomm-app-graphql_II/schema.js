const {gql} = require('apollo-server')

exports.typeDefs = gql`
    type Query {
        courses: [Course!]!
        course(id: ID!): Course
        genres: [Genre!]!
        genre(id: ID!): Genre
        welcome: String!
        numOfCourses: Int
        price: Float
        isTrainer: Boolean
    }

    type Course {
        id: ID!
        name: String!
        description: String!
        price: Float!
        discount: Boolean!
        genre: Genre
        reviews: [Review!]!
    }
    type Genre {
        id: ID!
        name: String!
        courses: [Course!]!
    }
    type Review {
        id: ID!
        date: String!
        title: String!
        comment: String!
        rating: Int!
    }
`