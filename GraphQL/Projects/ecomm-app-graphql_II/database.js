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

module.exports = {allCourses, genres}