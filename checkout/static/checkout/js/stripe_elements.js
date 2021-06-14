/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
    As well as the Boutique Ado Project from Code Institue Full Stack Frameworks
*/

var stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
var client_secret = $("#id_client_secret").text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var card = elements.create("card");

var style = {
    base: {
        color: "#000",
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: "antialiased",
        fontSize: "16px",
        "::placeholder": {
          color: "#aab7c4"
        }
    },
    invalid: {
        fontFamily: 'Arial, sans-serif',
        color: "#dc3545",
        iconColor: "#dc3545"
    }
  };

card.mount("#card-element", {stripe: style});