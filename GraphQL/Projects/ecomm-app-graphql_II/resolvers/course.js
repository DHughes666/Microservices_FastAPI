exports.Course = {
    genre: (parent, args, context) => {
        const db = context.db;
        const genreId = parent.genreId;
        return db.genres.find(item => item.id === genreId);
    },
    reviews: (parent, args, context) => {
        const db = context.db;
        const { id } = parent;
        return db.reviews.filter(item => item.courseId === id);
    }
}