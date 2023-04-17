describe(`${User.name} Class`, () => {
    let model;
    let mockUserService;

    beforeEach(() => {
        mockUserService = {
            lastId: null,
            user: {},
            getUserById(id) {
                this.lastId = id;

                return thia.user;
            }
        };
        const data = { firstName: 'Dylan', middleName: 'Christopher', lastName: 'Israel', id: 1};
        model = new User(data, mockUserService);
    });

    describe('getMyFullUserData', () => {
        it('gets user data by id', async () => {
            //arrange
            mockUserService.lastId = null;

            //act
            await model.getMyFullUserData();

            //assert
            expect(mockUserService.lastId).toBe(1);
        });
        it('gets full user data', async () => {
            //arrange
            mockUserService.user = new User({
                firstName: 'Juan',
                middleName: 'Llanos',
                lastName: 'Ordoñez',
                id: 2
            });
            //act
        });
    });
});