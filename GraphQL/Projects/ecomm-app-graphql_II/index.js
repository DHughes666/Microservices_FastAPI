const { ApolloServer, gql} = require('apollo-server')

const allCourses = [
    {   
        id: "book-01",
        name: "TypeScript Basics",
        description: "TypeScript Basics for beginners",
        price: 599.99,
        discount: false,
        genreId: "cat-02"
    },
    {
        id: "book-02",
        name: "GraphQL Basics",
        description: "GraphQL Basics for beginners",
        price: 499.99,
        discount: true,
        genreId: "cat-01"
    },
    {
        id: "book-03",
        name: "TypeScript Basics",
        description: "TypeScript Basics for beginners",
        price: 409.99,
        discount: true,
        genreId: "cat-02"
    },
    {
        id: "book-04",
        name: "NextJS Basics",
        description: "NextJS Basics for beginners",
        price: 739.09,
        discount: false,
        genreId: "cat-01",
    }
]

const genres = [
    {id: 'cat-01', name: 'Technical'},
    {id: 'cat-02', name: 'History'}
]

const typeDefs = gql`
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
    }
    type Genre {
        id: ID!
        name: String!
        courses: [Course!]!
    }
`

const resolvers = {
    Query: {
        courses: () => {
            return allCourses
        },
        course: (parent, args, context) => {
            const courseId = args.id;
            const course = allCourses.find(item => item.id === courseId);
            if(!course) return null;
            else return course
        },
        genres: () => genres,
        genre: (parent, args, context) => {
            const catId = args.id;
            const genre = genres.find(item => item.id === catId);
            if(!genre) return null;
            else return genre
        },
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
    },
    Genre: {
        courses: (parent, args, context) => {
            const genreId = parent.id;
            return allCourses.filter(item => item.genreId === genreId);
        }
    },
    Course: {
        genre: (parent, args, context) => {
            const genreId = parent.genreId;
            return genres.find(item => item.id === genreId);
        }
    }
}

const server = new ApolloServer({ typeDefs, resolvers });

server.listen().then(({url}) => console.log(`Server is running at ${url}`));