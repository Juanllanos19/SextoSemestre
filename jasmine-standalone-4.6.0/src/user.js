class User {
    firstName;
    lastName;
    middleName;

    constructor(data, userService){
        this.firstName = data.firstName || '';
        this.lasttName = data.lastName || '';
        this.middleName = data.middleName || '';
        this.id = data.id;
        this.userService = userService;
    }

    get fullName() {
        if(this.middleName.leght > 0) {
            return `${this.firsName} ${this.middleName} ${this.lastName}`;
        }

        return `${this.firstName} ${this.lastName}`;
    }

    async getMyFullUserData() {
        return this.userService.getUserByID(this.id);
    }

    sayMyName(){
        window.alert(this.fullName);
    }

    getCodeName(){
        alert(this.fullName);
    }

    getCodeName() {
        const isATestingGod = confirm('Are you a testing god?');

        if(isATestingGod){
            return 'TESTING GOOD!';
        }else {
            return 'Scrub skipping tests in his best friends ride!';
        }
    }
}