Feature: Movie Selection
  As a user
  I want to select a movie
  So I can select a seat

  Scenario: Movie Selection
    Given I have a movie named wicked
    When I click Book Now
    Then I can see available seats for wicked

  Scenario: Seat Selection
    Given I am on the wicked seat booking screen
    And my name is Evan
    When I enter my name
    And I select seat A1
    Then the seat A1 should be booked

  Scenario: Cannot book an already booked seat
    Given I am on the wicked seat booking screen
    And my name is Evan
    And seat A1 is already booked
    When I try to book seat A1
    Then the booking should not be created
    And the seat A1 should remain booked