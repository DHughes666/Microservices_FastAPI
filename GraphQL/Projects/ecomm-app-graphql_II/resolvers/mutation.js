const { v4: uuid } = require("uuid");

exports.Mutation = {
    addGenre: (parent, args, context) => {
        const {input} = args;
        const {name} = input;
        const {genres} = context;

        const newGenre = {id: uuid(), name}
        genres.push(newGenre)
        return newGenre;
    },
    addCourse: (parent, args, context) => {
        const {input} = args;
        const {name, description, price, discount, genreId} = input;
        const {allCourses} = context;

        const newCourse = {id: uuid(), name, 
            description, price, discount, genreId};
        allCourses.push(newCourse)
        return newCourse;
    }
}