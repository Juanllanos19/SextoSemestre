//Test Suites
describe(`${User.name} Class`, () => {
    it('exists', () => {
        expect(User).toBeDefined();
    });

    let model;

    beforeEach(() => {
        model = new User();
    });

    describe('additional matchers examples', () => {
        // toBeDefined(), toEqual()
        it('gets full name pieces', () => {
            //arrange
            const firstName = 'Dylan';
            const middleName =  'Christopher';
            const lastName = 'Israel';

            //act
            model = new User({firstName, middleName, lastName});

            //assert
            expect(model.fullNamePieces).toEqual([firstName, middleName, lastName]);
        });
    });
});