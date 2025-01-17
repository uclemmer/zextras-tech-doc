
.. index:: Lost password, password recovery

.. _password-recovery:

Lost Password
=============

If the Administrator has enabled the option, you can see a link
underneath the credential's text-fields, that allows you to recover
the password.

.. note:: Before you can start the password recovery procedure, you
   need to ask the Administrator to set up a recovery account for you.

When you click the *forgot Password* link, you will be asked to enter
your current username, the e-mail account (for example,
``john.smith@example.com``), then click the :bdg-primary:`SUBMIT`
button. Next, you need to confirm your e-mail recovery address. A
temporary *validation code*, that expires in a few minutes, will be
sent to the recovery e-mail address. Copy it and insert it, then click
the :bdg-primary:`VALIDATE CODE` button.

IF the code is validated, you can :bdg-primary-line:`CONTINUE WITH
YOUR SESSION`, access your mailbox and then add a new password in the
Settings's :ref:`settings-auth` module, where you can also change the
recovery address.

Active 2FA
----------

In case 2FA is active on |product|, there are two cases:

#. The request comes from a trustedIP (see Section :ref:`global-2fa`):
   this case is like the "standard" password recovery described in the
   above section

#. The request comes from an untrustedIP: you need to provide also an
   **OTP token** to be able to complete the recovery process
   
