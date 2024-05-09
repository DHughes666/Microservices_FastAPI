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

const reviews = [
    {
        id: "rev-01",
        date: "2021-01-01",
        title: "This is bad",
        comment: "When I bought this it broke the computer",
        rating: 1,
        courseId: "book-03",
    },
    {
        id: "rev-02",
        date: "2022-02-08",
        title: "This is awesome",
        comment: "Best book I ever bought",
        rating: 4,
        courseId: "book-04"
    }
]

exports.db = {allCourses, genres, reviews}