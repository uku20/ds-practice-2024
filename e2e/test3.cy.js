describe('Multiple Mixed Orders', () => {
    const orders = [
        { book: '#root > div > div.flex-grow-1 > div > div:nth-child(4) > div > div.col-md-4.d-flex.justify-content-center.align-items-center > a',checkout:'#root > div > div.flex-grow-1 > div > div > div:nth-child(2) > button', name: 'John Doe', contact: '123456', street: '123 Main St', city: 'tartu', state:'tartu', zip:'51009', country:'Estonia', creditCard: '4111111111111111', date:'06/28', cvv: '145', isFraudulent: false},
        { book:'#root > div > div.flex-grow-1 > div > div:nth-child(5) > div > div.col-md-4.d-flex.justify-content-center.align-items-center > a',checkout:'#root > div > div.flex-grow-1 > div > div > div:nth-child(2) > button', name: 'Jane Smith', contact: '123456', street: '223 Main St', city: 'tartu', state:'tartu', zip:'51009', country:'Estonia', creditCard: '41111111121', date:'04/28', cvv: '225', isFraudulent: true }
    ];

    orders.forEach((order) => {
        it(`should create a non-conflicting order for ${order.name}`, () => {
            cy.visit('http://localhost:8080');
            cy.get('#root > div > div.flex-grow-1 > div.p-5.mb-4.bg-dark.header > div > div > a').click(); 
            cy.get(order.book).click();
            cy.get(order.checkout).click();

            cy.get('#name').type(order.name);
            cy.get('#contact').type(order.contact);
            cy.get('#street').type(order.street);
            cy.get('#city').type(order.city);
            cy.get('#state').type(order.state);
            cy.get('#zip').type(order.zip);
        cy.get('#country').select(order.country); 
        cy.get('#creditCardNumbe').type(order.creditCard);
        cy.get('#creditCardExpirationDate').type(order.date);
        cy.get('#creditCardCVV').type(order.cvv);
        cy.get('#termsAndConditions').check();
        cy.get('#root > div > div.flex-grow-1 > div > form > button').click(); 
        cy.wait(10000);
        

if (order.isFraudulent) {
                // Verify fraud detection
                 cy.get('#root > div > div.flex-grow-1 > div').contains('Order Rejected').should('exist');

            } else {
                cy.get('#root > div > div.flex-grow-1 > div').contains('Order Approved').should('exist');

            }

            // Log the order creation
            cy.log(`${order.isFraudulent ? 'Fraudulent' : 'Non-fraudulent'} order handled for ${order.name}`);
        });
    });
});
