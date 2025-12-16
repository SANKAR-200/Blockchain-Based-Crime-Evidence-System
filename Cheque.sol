pragma solidity >= 0.8.11 <= 0.8.11;
pragma experimental ABIEncoderV2;
//cheque solidity code
contract Cheque {

    uint public chequeCount = 0; 
    mapping(uint => cheque) public chequeList; 
     struct cheque
     {
       string qrcode;
       string status;
     }
 
   // events 
   event chequeCreated(uint indexed _chequeId);

   function updateStatus(uint i) public { 
      chequeList[i].status = "Cleared";
   }
   //function  to save cheque as qr code hash values
   function createCheque(string memory _qrcode, string memory _status) public {
      chequeList[chequeCount] = cheque(_qrcode, _status);
      emit chequeCreated(chequeCount);
      chequeCount++;
    }

     //get cheque count
    function getChequeCount()  public view returns (uint) {
          return  chequeCount;
    }

    function getCode(uint i) public view returns (string memory) {
        cheque memory chq = chequeList[i];
	return chq.qrcode;
    }

    function getStatus(uint i) public view returns (string memory) {
        cheque memory chq = chequeList[i];
	return chq.status;
    }

     //get cheque details
    function getCheques()  public view returns (cheque[] memory){
       cheque[]    memory id = new cheque[](chequeCount);
      for (uint i = 0; i < chequeCount; i++) {
          cheque storage chq = chequeList[i];
          id[i] = chq;
      }
      return id;
    }
       
    uint public userCount = 0; 
    mapping(uint => user) public usersList; 
     struct user
     {
       string username;
       string email;
       string password;
       string phone;
       string home_address;
       string user_type;
     }
 
   // events
 
   event userCreated(uint indexed _userId);
 
  function createUser(string memory _username, string memory _email, string memory _password, string memory _phone, string memory _address, string memory _user_type) public {
      usersList[userCount] = user(_username, _email, _password, _phone, _address,  _user_type);
      emit userCreated(userCount);
      userCount++;
    }

     //get user details
    function getUser()  public view returns (user[] memory){
       user[]    memory id = new user[](userCount);
      for (uint i = 0; i < userCount; i++) {
          user memory usr = usersList[i];
          id[i] = usr;
      }
      return (id);
    }

     //get user count
    function getUserCount()  public view returns (uint) {
          return  userCount;
    }

    function getUsername(uint i) public view returns (string memory) {
        user memory usr = usersList[i];
	return usr.username;
    }

    function getPassword(uint i) public view returns (string memory) {
        user memory usr = usersList[i];
	return usr.password;
    }

    function getUsertype(uint i) public view returns (string memory) {
        user memory usr = usersList[i];
	return usr.user_type;
    }

    function getEmail(uint i) public view returns (string memory) {
        user memory usr = usersList[i];
	return usr.email;
    }
}