const { ApolloServer, gql} = require('apollo-server')

const typeDefs = gql`
    type Query {
        welcome: String
    }
`

const resolvers = {
    Query: {
        welcome: () => {
            return "Welcome to the World of GraphQL"
        }
    }
}

const server = new ApolloServer({ typeDefs, resolvers });

server.listen().then(({url}) => console.log(`Server is running at ${url}`));