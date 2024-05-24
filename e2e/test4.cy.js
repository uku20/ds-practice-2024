describe('Conflicting Orders', () => {
    const order1 = { book: '#root > div > div.flex-grow-1 > div > div:nth-child(4) > div > div.col-md-4.d-flex.justify-content-center.align-items-center > a',checkout:'#root > div > div.flex-grow-1 > div > div > div:nth-child(2) > button', name: 'John Doe', contact: '123456', street: '123 Main St', city: 'tartu', state:'tartu', zip:'51009', country:'Estonia', creditCard: '4111111111111111', date:'06/28', cvv: '145'};
    const order2 = { book:'#root > div > div.flex-grow-1 > div > div:nth-child(5) > div > div.col-md-4.d-flex.justify-content-center.align-items-center > a',checkout:'#root > div > div.flex-grow-1 > div > div > div:nth-child(2) > button', name: 'Jane Smith', contact: '123456', street: '223 Main St', city: 'tartu', state:'tartu', zip:'51009', country:'Estonia', creditCard: '4111111112211111', date:'04/28', cvv: '225' };

    it('should handle conflicting orders', () => {
            cy.visit('http://localhost:8080');
            cy.get('#root > div > div.flex-grow-1 > div.p-5.mb-4.bg-dark.header > div > div > a').click(); 
            cy.get(order1.book).click();
            cy.get(order1.checkout).click();

            cy.get('#name').type(order1.name);
            cy.get('#contact').type(order1.contact);
            cy.get('#street').type(order1.street);
            cy.get('#city').type(order1.city);
            cy.get('#state').type(order1.state);
            cy.get('#zip').type(order1.zip);
            cy.get('#country').select(order1.country); 
            cy.get('#creditCardNumbe').type(order1.creditCard);
            cy.get('#creditCardExpirationDate').type(order1.date);
            cy.get('#creditCardCVV').type(order1.cvv);
            cy.get('#termsAndConditions').check();
            cy.get('#root > div > div.flex-grow-1 > div > form > button').click(); 
            cy.wait(8000);
            
           cy.log('First non-fraudulent order created for John Doe');

        // Introduce delay before second order to simulate concurrency
        cy.wait(500);

        // Second Order
            cy.visit('http://localhost:8080');
            cy.get('#root > div > div.flex-grow-1 > div.p-5.mb-4.bg-dark.header > div > div > a').click(); 
            cy.get(order2.book).click();
            cy.get(order2.checkout).click();

            cy.get('#name').type(order2.name);
            cy.get('#contact').type(order2.contact);
            cy.get('#street').type(order2.street);
            cy.get('#city').type(order2.city);
            cy.get('#state').type(order2.state);
            cy.get('#zip').type(order2.zip);
            cy.get('#country').select(order2.country); 
            cy.get('#creditCardNumbe').type(order2.creditCard);
            cy.get('#creditCardExpirationDate').type(order2.date);
            cy.get('#creditCardCVV').type(order2.cvv);
            cy.get('#termsAndConditions').check();
            cy.get('#root > div > div.flex-grow-1 > div > form > button').click(); 
            cy.wait(10000);
                     cy.get('#root > div > div.flex-grow-1 > div').contains('Order Approved').should('exist');
        // Log the second order creation
        cy.log('Second non-fraudulent order created for Jane Smith');
    });
});