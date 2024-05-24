describe('Single Non-Fraudulent Order', () => {
    it('should create a non-fraudulent order and verify its correctness', () => {
        cy.visit('localhost:8080'); // Navigate to the homepage
 
       
        cy.get('#root > div > div.flex-grow-1 > div.p-5.mb-4.bg-dark.header > div > div > a').click(); 
        cy.get('#root > div > div.flex-grow-1 > div > div:nth-child(4) > div > div.col-md-4.d-flex.justify-content-center.align-items-center > a').click();
        cy.get('#root > div > div.flex-grow-1 > div > div > div:nth-child(2) > button').click();
        cy.get('#name').type('John Doe'); // Fill in name
        cy.get('#contact').type('123456');
        cy.get('#street').type('123 Main St');
        cy.get('#city').type('tartu');
        cy.get('#state').type('tartu');
        cy.get('#zip').type('51009');
        cy.get('#country').select('Estonia'); 
        cy.get('#creditCardNumbe').type('4111111111111111');
        cy.get('#creditCardExpirationDate').type('08/27');
        cy.get('#creditCardCVV').type('000');
        cy.get('#termsAndConditions').check();
        cy.get('#root > div > div.flex-grow-1 > div > form > button').click(); 
        cy.wait(10000);
        // Verify order details
        cy.get('#root > div > div.flex-grow-1 > div').contains('Order Approved').should('exist');
        
        
        // Log the order creation
        cy.log('Single non-fraudulent order created and verified for correctness');
    });
});
