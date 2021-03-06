// ledTimeOn.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <../ledTimeOn/HCNetSDK.h>
#include <stdio.h>
#include <iostream>
#include "Windows.h"
#include "HCNetSDK.h"
#include <time.h>
using namespace std;



void main() {
	//---------------------------------------
	// Initialize
	NET_DVR_Init();
	// Set connected time and reconnected time
	NET_DVR_SetConnectTime(2000, 1);
	NET_DVR_SetReconnect(10000, true);

	//---------------------------------------
	// Register device
	LONG lUserID;

	//Login parameters, including device IP address, user name, password
	NET_DVR_USER_LOGIN_INFO struLoginInfo = { 0 };
	struLoginInfo.bUseAsynLogin = 0; //Sync login method
	strcpy_s(struLoginInfo.sDeviceAddress, ""); //Device IP address
	struLoginInfo.wPort = 8000; //Device service port
	strcpy_s(struLoginInfo.sUserName, ""); //Device user name
	strcpy_s(struLoginInfo.sPassword, ""); //Device password

	//Device information, output parameters
	NET_DVR_DEVICEINFO_V40 struDeviceInfoV40 = { 0 };

	lUserID = NET_DVR_Login_V40(&struLoginInfo, &struDeviceInfoV40);
	if (lUserID < 0)
	{
		printf("Login failed, error code: %d\n", NET_DVR_GetLastError());
		NET_DVR_Cleanup();
		return;
	}

	NET_DVR_PDC_QUERY_COND m_struPdcResultCond = { 0 };
	m_struPdcResultCond.dwSize = sizeof(m_struPdcResultCond);//Condition for searching people counting data
	m_struPdcResultCond.dwChannel = 1; //Device channel No.
	

	struct tm tim;
	time_t tt = time(NULL);

	localtime_s(&tim, &tt);

	int theDay = tim.tm_mday;
	int theMonth = tim.tm_mon;
	int theYear = tim.tm_year + 1900;
	printf("%d.%d.%d", theYear, theMonth, theDay); // или std::cout << theYear << "." << theMonth << "."

	
	//Start time of search
	m_struPdcResultCond.struStartTime.wYear = theYear;
	m_struPdcResultCond.struStartTime.byMonth = theMonth+1;
	m_struPdcResultCond.struStartTime.byDay = theDay;
	m_struPdcResultCond.struStartTime.byHour = 00;
	m_struPdcResultCond.struStartTime.byMinute = 00;
	m_struPdcResultCond.struStartTime.bySecond = 00;
	
	//End time of search
	 
	m_struPdcResultCond.struEndTime.wYear = theYear;
	m_struPdcResultCond.struEndTime.byMonth = theMonth+1;
	m_struPdcResultCond.struEndTime.byDay = theDay;
	m_struPdcResultCond.struEndTime.byHour = 00;
	m_struPdcResultCond.struEndTime.byMinute = 00;
	m_struPdcResultCond.struEndTime.bySecond = 00;
	

	m_struPdcResultCond.byReportType = 2; //Search type:0- invalid, 1- daily report, 2- weekly report, 3- monthly report, 4- annual report
	int count = 0;
	LONG m_lHandle = NET_DVR_StartRemoteConfig(lUserID, NET_DVR_GET_PDC_RESULT, &m_struPdcResultCond, sizeof(m_struPdcResultCond), NULL, NULL);
	if (m_lHandle >= 0)
	{

		LONG iNextRet = 0;
		NET_DVR_PDC_RESULT m_struPdcResult = { 0 };
		while (true)
		{
			
			iNextRet = NET_DVR_GetNextRemoteConfig(m_lHandle, &m_struPdcResult, sizeof(NET_DVR_PDC_RESULT));
			if (iNextRet == NET_SDK_GET_NEXT_STATUS_SUCCESS) //Data found.
			{
				if (m_struPdcResult.dwEnterNum!=0 && m_struPdcResult.dwLeaveNum!=0){
					printf("StartTime[%4.4d-%2.2d-%2.2d %2.2d:%2.2d:%2.2d]EndTime[%4.4d-%2.2d-%2.2d %2.2d:%2.2d:%2.2d],dwEnterNum[%d]dwLeaveNum[%d]\n", \
						m_struPdcResult.struStartTime.wYear, m_struPdcResult.struStartTime.byMonth, m_struPdcResult.struStartTime.byDay, \
						m_struPdcResult.struStartTime.byHour, m_struPdcResult.struStartTime.byMinute, m_struPdcResult.struStartTime.bySecond, \
						m_struPdcResult.struEndTime.wYear, m_struPdcResult.struEndTime.byMonth, m_struPdcResult.struEndTime.byDay, \
						m_struPdcResult.struEndTime.byHour, m_struPdcResult.struEndTime.byMinute, m_struPdcResult.struEndTime.bySecond,
						m_struPdcResult.dwEnterNum, m_struPdcResult.dwLeaveNum);

					std::cout << "enter : " << m_struPdcResult.dwEnterNum << " , leave : " << m_struPdcResult.dwLeaveNum << std::endl;
					count++;
				}
				else {
					//continue;
					break;
				}
				
			}
			/*
			else
			{
				if (iNextRet == NET_SDK_GET_NETX_STATUS_NEED_WAIT) //Wait for device to send data
				{
					Sleep(5);
					continue;
				}
				if (iNextRet == NET_SDK_GET_NEXT_STATUS_FINISH) //Searching all data ended.
				{
					printf("People counting data search end!\n");
					break;
				}
				else if (iNextRet == NET_SDK_GET_NEXT_STATUS_FAILED) //Search exception
				{
					printf("Search exception.\n");
					break;
				}
				else
				{
					printf("Unknown status.\n");
					break;
				}
			}
			*/

		}
	}
	else
	{
		printf("Searching people counting data failed. Error code: %d\n", NET_DVR_GetLastError());
	}

	if (m_lHandle >= 0)
	{
		if (!NET_DVR_StopRemoteConfig(m_lHandle))
		{
			printf("Failed to stop people counting data search. Error code: %d\n", NET_DVR_GetLastError());
		}
	}

	//User logout
	NET_DVR_Logout(lUserID);
	//Release SDK resource
	NET_DVR_Cleanup();
	std::cout << "count : " << count << std::endl;
	return;
}

