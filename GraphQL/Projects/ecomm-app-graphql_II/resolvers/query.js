const {courses, genres} = require('../database');


exports.Query = {
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
    }
}