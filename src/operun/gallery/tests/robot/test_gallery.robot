# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s operun.gallery -t test_gallery.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src operun.gallery.testing.OPERUN_GALLERY_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_gallery.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Gallery
  Given a logged-in site administrator
    and an add gallery form
   When I type 'My Gallery' into the title field
    and I submit the form
   Then a gallery with the title 'My Gallery' has been created

Scenario: As a site administrator I can view a Gallery
  Given a logged-in site administrator
    and a gallery 'My Gallery'
   When I go to the gallery view
   Then I can see the gallery title 'My Gallery'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add gallery form
  Go To  ${PLONE_URL}/++add++Gallery

a gallery 'My Gallery'
  Create content  type=Gallery  id=my-gallery  title=My Gallery


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the gallery view
  Go To  ${PLONE_URL}/my-gallery
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a gallery with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the gallery title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
