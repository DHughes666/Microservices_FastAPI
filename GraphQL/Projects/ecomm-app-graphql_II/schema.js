const {gql} = require('apollo-server')

exports.typeDefs = gql`
    type Query {
        courses(filter: CoursesFilter): [Course!]!
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
        courses(filter: CoursesFilter): [Course!]!
    }
    type Review {
        id: ID!
        date: String!
        title: String!
        comment: String!
        rating: Int!
    }

    input CoursesFilter {
        discount: Boolean
        avgRating: Int
    }

    type Mutation {
        addGenre(input: AddGenreInput!): Genre!
    }
    input AddGenreInput {
        name: String!
    }
`