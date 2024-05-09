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
    },
    deleteCourse: (parent, {id}, {db}) => {
        db.allCourses = db.allCourses.filter(course => 
            course.id !== id);
        db.reviews = db.reviews.filter(review => review.courseId !== id);
        return true;
    },
    deleteReview: (parent, {id}, {db}) => {
        db.reviews = db.reviews.filter(review => review.id !== id);
        return true;
    },
    updateGenre: (parent, {id, input }, {db}) => {
        const index = db.genres.findIndex(genre => genre.id === id);
        if(index === -1) return null;
        db.genres[index] = {...db.genres[index], ...input};
        return db.genres[index];
    },
    updateCourse: (parent, {id, input}, {db}) => {
        const index = db.allCourses.findIndex(course => course.id === id);
        if(index === -1) return null;
        db.allCourses[index] = {...db.allCourses[index], ...input};
        return db.allCourses[index];
    },
    updateReview: (parent, {id, input}, {db}) => {
        const index = db.reviews.findIndex(review => review.id === id);
        db.reviews[index] = {...db.reviews[index], ...input};
        return db.reviews[index];
    }
}