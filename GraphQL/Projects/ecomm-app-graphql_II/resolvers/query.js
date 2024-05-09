exports.Query = {
    courses: (parent, args, {db}) => {
        let filteredCourses = db.allCourses;
        const { filter } = args;
        if(filter){
            const { discount, avgRating } = filter;
            if(discount) filteredCourses = filteredCourses.filter(
                product => product.discount
            );
            if([1, 2, 3, 4, 5].includes(avgRating)) {
                filteredCourses = filteredCourses.filter(
                    item => {
                        let sum = 0;
                        let numOfReviews = 0;
                        db.reviews.forEach((review) => {
                            if(review.courseId === item.id){
                                sum += review.rating;
                                numOfReviews ++;
                            }
                        })
                        const avgCourseRating = sum / numOfReviews;
                        return avgCourseRating >= avgRating
                    }
                )
            }
        }
        return filteredCourses;
    },
    course: (parent, args, {db}) => {
        const courseId = args.id;
        const course = db.courses.find(item => item.id === courseId);
        if(!course) return null;
        else return course
    },
    genres: (parent, args, {db}) => {
        const genres = db.genres;
        return genres
    },
    genre: (parent, args, {db}) => {
        const catId = args.id;
        const genre = db.genres.find(item => item.id === catId);
        if(!genre) return null;
        else return genre
    }
}