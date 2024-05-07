const { ApolloServer, gql} = require('apollo-server')

const typeDefs = gql`
    type Query {
        welcome: String!
        numOfCourses: Int
        price: Float
        isTrainer: Boolean
    }
`

const resolvers = {
    Query: {
        welcome: () => {
            return "We are here"
        },
        numOfCourses: () => {
            return 12;
        },
        price: () => {
            return 1465.98;
        },
        isTrainer: () => {
            return true;
        }
    }
}

const server = new ApolloServer({ typeDefs, resolvers });

server.listen().then(({url}) => console.log(`Server is running at ${url}`));