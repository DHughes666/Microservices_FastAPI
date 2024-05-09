const { v4: uuid } = require("uuid");

exports.Mutation = {
    addGenre: (parent, args, {db}) => {
        const {input} = args;
        const {name} = input;
        const newGenre = {id: uuid(), name}
        db.genres.push(newGenre)
        return newGenre;
    },
    addCourse: (parent, args, {db}) => {
        const {input} = args;
        const {name, description, price, discount, genreId} = input;
        const newCourse = {id: uuid(), name, 
            description, price, discount, genreId};
        db.allCourses.push(newCourse)
        return newCourse;
    },
    addReview: (parent, args, {db}) => {
        const {input} = args;
        const {date, title, comment, rating, courseId} = input;
        const newReview = {id: uuid(), date, title, 
            comment, rating, courseId}
        db.reviews.push(newReview)
        return newReview
    },
    deleteGenre: (parent, {id}, {db}) => {
        db.genres = db.genres.filter(genre => genre.id !== id);
        db.allCourses = db.allCourses.map(course => {
            if(course.genreId === id){
                return {...course, genreId: null}
            } else {
                return course
            }
        })
        return true;
    }
}