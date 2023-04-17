class UserService{
    getUserByID(id) {
        return fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
    }
}