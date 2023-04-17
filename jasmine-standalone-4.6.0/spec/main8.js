// Test Suite
describe(`${User.name} Class`, () => {
    let model;

    beforeEach(() => {
        model = new User();
    });

    describe('additional matchers testing area', () => {
        it('has my first name', () => {
            //arrange
            const firstName = 'Juan';
            const lastName = 'Llanos';

            //act
            model = new User({firstName, lastName});

            //assert
            expect(model.fullName).toMatch(/Juan/);
        });
    });
});