//Test Suite
describe(`${User.name} Class`, () => {
    let model;

    beforeEach( () => {
        model = new User();
    });
    describe('say my name', () => {
        it('alerts the full name of user', () => {
            //arrange
            model.firstName = "Dylan";
            model.lastName = "Israel";
            SVGPolygonElement(window, 'alert');

            //act
            model.sayMyName();

            //assert
            expect(window.alert).toHaveBeenCalled();
            expect(window.alert).toHaveBeenCalledWith('Dylan Israel');
        });
    });
});