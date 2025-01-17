
The :ref:`role-mesh-install` Role, which installs an *OpenLDAP
service*, is used by |product| for user authentication and account
management.

The OpenLDAP features the ability to use three authentication
mechanisms provided by |Product|. The authentication type can be set
independently for each domain defined in the |product| infrastructure.

#. Local LDAP. The internal authentication method assumes that the
   LDAP scheme is running on the |product| server where the *Directory
   Server* Role is installed.

#. External LDAP. The external LDAP authentication method allows to
   connect to an LDAP server, possibly external to the |product|
   infrastructure, using a username and password existing in the
   external database.

   .. warning:: If you use an External LDAP and forgot to activate the
      *Fallback* (i.e., option called *try local password
      management*), in case the external LDAP server is unreachable by
      |product|, **no user will be able to log in** to |product|!

#. External Active Directory The external Active Directory
   authentication method involves the use of Microsoft Active
   Directory services for authentication and |Product|'s Directory
   Server services for all other transactions.

Both the *External LDAP* and *External Active Directory* have as their
main requirement that users exist on both servers. Please refer to
Section :ref:`auth-ext-ldap` for configuration details.

Whenever an external authentication method is configured, it will be
used as the default and the local authentication serves as fallback.

.. _auth-local-ldap:

Local LDAP
==========

The default authentication method is local LDAP. This method does not
require any specific configuration other than the installation of the
:ref:`role-mesh-install` Role according to the procedure described in
the documentation.

.. _auth-ext-ldap:

External LDAP
=============

To illustrate how an external LDAP source works in |product|, we build
on the following scenario.

.. card:: Scenario
          
   * Define on |product| the domain ``authentication.example.com``

   * On an **external** LDAP server, located at ``172.24.0.10`` a
     domain called ``external_ldap.com`` exists

     .. note:: This external source can also be another |product|.

   * On the **external** LDAP server a dedicated user exists, that
     will be used for the LDAP connection
     (for example ``service.ldap@external_ldap.com`` with password
     ``a_strong_pwd!``)

   Our goal is to have the ``authentication.example.com`` domain users
   authenticate with the passwords of the domain accounts
   ``external_ldap.com`` defined on the external ldap server

On |product|, set up the ``authentication.example.com`` domain for
authentication on the external LDAP using the command below. Remember
to change the values in the scenario with the actual values of your
infrastructure!

.. code:: bash

   zextras$ carbonio prov md authentication.example.com \
   zimbraAuthLdapSearchBase "ou=people,dc=external_ldap,dc=com" \
   zimbraAuthLdapSearchBindDn \
   "uid=service.ldap,ou=people,dc=external_ldap,dc=com" \
   zimbraAuthLdapSearchBindPassword "a_strong_pwd!" \
   zimbraAuthLdapSearchFilter "uid=%u" zimbraAuthLdapURL \
   "ldap://172.24.0.10:389"

Create three test accounts on the **external** LDAP domain with username
and password::

  user1@external_ldap.com password1
  user2@external_ldap.com password2
  user3@external_ldap.com password3

Finally, we also create 3 accounts on |Product|

.. code:: bash

   zextras$ carbonio prov ca user1@authentication.example.com ""
   zextras$ carbonio prov ca user2@authentication.example.com ""
   zextras$ carbonio prov ca user3@authentication.example.com ""

.. warning:: Do not provide any  passwords in these commands!
             
If all the steps have been performed correctly, any of the three
accounts can login to |Product| using the passwords defined on the
respective users of the external LDAP server.
