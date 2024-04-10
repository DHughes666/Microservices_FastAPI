const { ApolloServer, gql } = require("apollo-server");


const allCourses = [
    {
        name: "TypeScript Basics",
        description: "TypeScript Basics for beginners",
        price: 599.99,
        discount: false
    },
    {
        name: "NextJS Basics",
        description: "NextJS Basics for beginners",
        price: 759.99,
        discount: false
    },
    {
        name: "GraphQL Basics",
        description: "GraphQL Basics for beginners",
        price: 219.99,
        discount: true
    }
]

const typeDefs = gql`
    type Query {
        courses: [Course!]!
    }

    type Course {
        name: String!
        description: String!
        price: Float!
        discount: Boolean!
    }
`

const resolvers = {
    Query: {
        courses: () => {
            return allCourses
        },
    }
}

const server = new ApolloServer({typeDefs, resolvers})

server.listen().then(
    ({ url }) => console.log(`Server listening on ${url}`));