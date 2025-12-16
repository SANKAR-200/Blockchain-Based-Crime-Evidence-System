pragma solidity >= 0.8.11 <= 0.8.11;
pragma experimental ABIEncoderV2;
//Evidence solidity code
contract Evidence {

    uint public evidenceCount = 0; 
    mapping(uint => evidence) public evidenceList; 
     struct evidence
     {
       string evidence_id;
       string officer_name;
       string reported_crime;
       string crime_details;
       string evidence_details;
       string crime_area;
       string witness_name;
       string witness_contact;
       string crime_date;       
     }
 
   // events 
   event evidenceCreated(uint indexed _evidenceId);

  
   //function  to save evidence details
   function createEvidence(string memory eid, string memory oname, string memory crime, string memory cd, string memory ed, string memory ca, string memory wn, string memory wc, string memory crime_dd) public {
      evidenceList[evidenceCount] = evidence(eid, oname, crime, cd, ed, ca, wn, wc, crime_dd);
      emit evidenceCreated(evidenceCount);
      evidenceCount++;
    }

     //get evidence count
    function getEvidenceCount()  public view returns (uint) {
          return  evidenceCount;
    }

    function getEvidenceid(uint i) public view returns (string memory) {
        evidence memory chq = evidenceList[i];
	return chq.evidence_id;
    }

    function getOfficername(uint i) public view returns (string memory) {
        evidence memory chq = evidenceList[i];
	return chq.officer_name;
    }      

    function getReportedcrime(uint i) public view returns (string memory) {
        evidence memory chq = evidenceList[i];
	return chq.reported_crime;
    }

    function getCrimedetails(uint i) public view returns (string memory) {
        evidence memory chq = evidenceList[i];
	return chq.crime_details;
    }     
   
    function getEvidencedetails(uint i) public view returns (string memory) {
        evidence memory chq = evidenceList[i];
	return chq.evidence_details;
    }

    function getCrimearea(uint i) public view returns (string memory) {
        evidence memory chq = evidenceList[i];
	return chq.crime_area;
    }

    function getWitnessname(uint i) public view returns (string memory) {
        evidence memory chq = evidenceList[i];
	return chq.witness_name;
    }

    function getCrimedate(uint i) public view returns (string memory) {
        evidence memory chq = evidenceList[i];
	return chq.crime_date;
    }

    function getWitnesscontact(uint i) public view returns (string memory) {
        evidence memory chq = evidenceList[i];
	return chq.witness_contact;
    }
           
    uint public userCount = 0; 
    mapping(uint => user) public usersList; 
     struct user
     {
       string username;
       string password;
       string phone;
       string email;
       string station_address;
     }
 
   // events
 
   event userCreated(uint indexed _userId);
 
  function createUser(string memory _username, string memory _password, string memory _phone, string memory em, string memory sa) public {
      usersList[userCount] = user(_username, _password, _phone, em, sa);
      emit userCreated(userCount);
      userCount++;
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

    function getPhone(uint i) public view returns (string memory) {
        user memory usr = usersList[i];
	return usr.phone;
    }

    function getEmail(uint i) public view returns (string memory) {
        user memory usr = usersList[i];
	return usr.email;
    }

    function getStationaddress(uint i) public view returns (string memory) {
        user memory usr = usersList[i];
	return usr.station_address;
    }
}