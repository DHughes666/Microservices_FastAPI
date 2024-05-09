exports.Genre = {
    courses: (parent, args, context) => {
        const {db} = context;
        const genreId = parent.id;
        const { filter } = args;
        const genreProducts = db.allCourses.filter(
            item => item.genreId === genreId);
        let filteredGenre = genreProducts;
        if(filter){
            if(filter.discount){
                filteredGenre = filteredGenre.filter(
                    product => product.discount
                );
            }
        }
        return filteredGenre;
    }
}