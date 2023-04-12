class User {
    firstName;
    lastName;
    middleName;

    constructor(data = {}){
        this.firstName = data.firstName || '';
        this.lasttName = data.lastName || '';
        this.middleName = data.middleName || '';
    }
}